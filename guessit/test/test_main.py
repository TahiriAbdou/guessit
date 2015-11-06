#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=no-self-use, pointless-statement, missing-docstring, invalid-name

import os

import pytest

from ..__main__ import main

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def test_main_no_args():
    main([])


def test_main():
    main([u'Fear.and.Loathing.in.Las.Vegas.FRENCH.ENGLISH.720p.HDDVD.DTS.x264-ESiR.mkv'])


def test_main_unicode():
    main([u'[阿维达].Avida.2006.FRENCH.DVDRiP.XViD-PROD.avi'])


def test_main_non_unicode():
    main(['Fear.and.Loathing.in.Las.Vegas.FRENCH.ENGLISH.720p.HDDVD.DTS.x264-ESiR.mkv'])


def test_main_verbose():
    main([u'Fear.and.Loathing.in.Las.Vegas.FRENCH.ENGLISH.720p.HDDVD.DTS.x264-ESiR.mkv', '--verbose'])


def test_main_yaml():
    main([u'Fear.and.Loathing.in.Las.Vegas.FRENCH.ENGLISH.720p.HDDVD.DTS.x264-ESiR.mkv', '--yaml'])


def test_main_json():
    main([u'Fear.and.Loathing.in.Las.Vegas.FRENCH.ENGLISH.720p.HDDVD.DTS.x264-ESiR.mkv', '--json'])


def test_main_show_property():
    main([u'Fear.and.Loathing.in.Las.Vegas.FRENCH.ENGLISH.720p.HDDVD.DTS.x264-ESiR.mkv', '-P', 'title'])


def test_main_advanced():
    main([u'Fear.and.Loathing.in.Las.Vegas.FRENCH.ENGLISH.720p.HDDVD.DTS.x264-ESiR.mkv', '-a'])


def test_main_input():
    main(['--input', os.path.join(__location__, 'test-input-file.txt')])


def test_main_help():
    with pytest.raises(SystemExit):
        main(['--help'])


def test_main_version():
    main(['--version'])
