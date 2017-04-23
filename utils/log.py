#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s_%(filename)s@line:%(lineno)d %(levelname)s: %(message)s',
                    datefmt='%H:%M:%S')
log = logging.getLogger(__name__)
