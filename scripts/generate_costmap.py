#!/usr/bin/env python
#
# Copyright (c) 2014 Garrett Brown
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import addon
import costmap
import geometry
import pathfinder

try:
    import numpy as np
except ImportError:
    print('Error importing numpy (try sudo apt-get install python-numpy)')
    sys.exit(1)

try:
    import cv2
except ImportError:
    print('Error importing cv2 (try sudo apt-get install python-opencv)')
    sys.exit(1)

def main():
    ad = addon.Addon('addon.xml')
    if ad.IsValid():
        cm = costmap.Costmap(ad.LayoutWidth(), ad.LayoutHeight(), ad.Buttons())
        #cm.Show()
        cm.Save(ad.CostmapImage())

        goal = geometry.Vector(geometry.Point(0, ad.LayoutHeight() / 2), geometry.DIRECTION_LEFT)

        pf = pathfinder.PathFinder(cm, ad.Buttons()[0].StartPoints()[0], goal)
        img = cv2.imread(ad.LayoutImage(), cv2.IMREAD_UNCHANGED)
        pf.Render(img, 'path1.png')


if __name__ == '__main__':
    main()

