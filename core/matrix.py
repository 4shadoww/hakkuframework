# Copyright (c) 2012 Tom Wallroth
#
# Sources on github:
#   http://github.com/devsnd/matrix-curses/
#
# licensed under GNU GPL version 3 (or later)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from __future__ import unicode_literals
import locale
import time
import curses
import random
from collections import namedtuple
import sys
PYTHON2 = sys.version_info.major < 3
locale.setlocale(locale.LC_ALL, '')
encoding = locale.getpreferredencoding()

########################################################################
# TUNABLES

DROPPING_CHARS = 50
MIN_SPEED = 1
MAX_SPEED = 7
RANDOM_CLEANUP = 100
WINDOW_CHANCE = 50
WINDOW_SIZE = 25
WINDOW_ANIMATION_SPEED = 3
FPS = 25
SLEEP_MILLIS = 1.0/FPS
USE_COLORS = True
SCREENSAVER_MODE = True
MATRIX_CODE_CHARS = "ɀɁɂŧϢϣϤϥϦϧϨϫϬϭϮϯϰϱϢϣϤϥϦϧϨϩϪϫϬϭϮϯϰ߃߄༣༤༥༦༧༩༪༫༬༭༮༯༰༱༲༳༶"

########################################################################
# CODE

COLOR_CHAR_NORMAL = 1
COLOR_CHAR_HIGHLIGHT = 2
COLOR_WINDOW = 3

class FallingChar(object):
    matrixchr = list(MATRIX_CODE_CHARS)
    normal_attr = curses.A_NORMAL
    highlight_attr = curses.A_REVERSE        
    
    def __init__(self, width, MIN_SPEED, MAX_SPEED):
        self.x = 0
        self.y = 0
        self.speed = 1
        self.char = ' '
        self.reset(width, MIN_SPEED, MAX_SPEED)
    
    def reset(self, width, MIN_SPEED, MAX_SPEED):
        self.char = random.choice(FallingChar.matrixchr).encode(encoding)
        self.x = randint(1, width - 1)
        self.y = 0
        self.speed = randint(MIN_SPEED, MAX_SPEED)
        # offset makes sure that chars with same speed don't move all in same frame
        self.offset = randint(0, self.speed)
    
    def tick(self, scr, steps):
        height, width = scr.getmaxyx()
        if self.advances(steps):
            # if window was resized and char is out of bounds, reset
            self.out_of_bounds_reset(width, height)
            # make previous char curses.A_NORMAL
            if USE_COLORS:
                scr.addstr(self.y, self.x, self.char, curses.color_pair(COLOR_CHAR_NORMAL))
            else:
                scr.addstr(self.y, self.x, self.char, curses.A_NORMAL)
                
            # choose new char and draw it A_REVERSE if not out of bounds
            self.char = random.choice(FallingChar.matrixchr).encode(encoding)
            self.y += 1
            if not self.out_of_bounds_reset(width, height):
                if USE_COLORS:
                    scr.addstr(self.y, self.x, self.char, curses.color_pair(COLOR_CHAR_HIGHLIGHT))
                else:
                    scr.addstr(self.y, self.x, self.char, curses.A_REVERSE)
    
    def out_of_bounds_reset(self, width, height):
        if self.x > width-2:
            self.reset(width, MIN_SPEED, MAX_SPEED)
            return True
        if self.y > height-2:
            self.reset(width, MIN_SPEED, MAX_SPEED)
            return True
        return False
    
    def advances(self, steps):
        if steps % (self.speed + self.offset) == 0:
            return True
        return False
    
    def step(self, steps, scr):
       
        return -1, -1, None

class WindowAnimation(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.step = 0
        
    def tick(self, scr, steps):
        if self.step > WINDOW_SIZE:
            #stop window animation after some steps
            self.draw_frame(scr, self.x - self.step, self.y - self.step,
                            self.x + self.step, self.y + self.step,
                            curses.A_NORMAL)
            return False
        
        # clear all characters covered by the window frame
        for i in range(WINDOW_ANIMATION_SPEED):
            anistep = self.step + i
            self.draw_frame(scr, self.x - anistep, self.y - anistep,
                            self.x + anistep, self.y + anistep,
                            curses.A_NORMAL, ' ')
        #cancel last animation
        self.draw_frame(scr, self.x - self.step, self.y - self.step,
                        self.x + self.step, self.y + self.step,
                        curses.A_NORMAL)
        #next step
        self.step += WINDOW_ANIMATION_SPEED
        
        #draw outer frame
        self.draw_frame(scr, self.x - self.step, self.y - self.step,
                        self.x + self.step, self.y + self.step,
                        curses.A_REVERSE)
        return True

    def draw_frame(self, scr, x1, y1, x2, y2, attrs, clear_char=None):
        if USE_COLORS:
            if attrs == curses.A_REVERSE:
                attrs = curses.color_pair(COLOR_WINDOW)
        h, w = scr.getmaxyx()
        for y in (y1, y2):
            for x in range(x1, x2+1):
                if x < 0 or x > w-1 or y < 0 or y > h-2:
                    continue
                if clear_char is None:
                    scr.chgat(y, x, 1, attrs)
                else:
                    scr.addstr(y, x, clear_char, attrs)
        for x in (x1, x2):
            for y in range(y1, y2+1):
                if x < 0 or x > w-1 or y < 0 or y > h-2:
                    continue
                if clear_char is None:
                    scr.chgat(y, x, 1, attrs)
                else:
                    scr.addstr(y, x, clear_char, attrs)


# we don't need a good PRNG, just something that looks a bit random.
def rand():
    # ~ 2 x as fast as random.randint
    a = 9328475634
    while True:
        a ^= (a << 21) & 0xffffffffffffffff;
        a ^= (a >> 35);
        a ^= (a << 4) & 0xffffffffffffffff;
        yield a

r = rand()
def randint(_min, _max):
    if PYTHON2:
        n = r.next()# pylint: disable=no-member
    else:
        n = r.__next__()
    return (n % (_max - _min)) + _min

def main():
    steps = 0
    scr = curses.initscr()
    scr.nodelay(1)
    curses.curs_set(0)
    curses.noecho()
    
    if USE_COLORS:
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(COLOR_CHAR_NORMAL, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(COLOR_CHAR_HIGHLIGHT, curses.COLOR_WHITE, curses.COLOR_GREEN)
        curses.init_pair(COLOR_WINDOW, curses.COLOR_GREEN, curses.COLOR_GREEN)
    
    height, width = scr.getmaxyx()    
    window_animation = None
    lines = []
    for i in range(DROPPING_CHARS):
        l = FallingChar(width, MIN_SPEED, MAX_SPEED)
        l.y = randint(0, height-2)
        lines.append(l)
        
    scr.refresh()
    while True:
        height, width = scr.getmaxyx()
        for line in lines:
            line.tick(scr, steps)
        for i in range(RANDOM_CLEANUP):
            x = randint(0, width-1)
            y = randint(0, height-1)
            scr.addstr(y, x, ' ')
        if randint(0, WINDOW_CHANCE) == 1:
            if window_animation is None:
                #start window animation
                line = random.choice(lines)
                window_animation = WindowAnimation(line.x, line.y)
        if not window_animation is None:
           still_active = window_animation.tick(scr, steps)
           if not still_active:
               window_animation = None

        scr.refresh()
        time.sleep(SLEEP_MILLIS)
        if SCREENSAVER_MODE:
            key_pressed = scr.getch() != -1
            if key_pressed:
                raise KeyboardInterrupt()
        steps += 1

