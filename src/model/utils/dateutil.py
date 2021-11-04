#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from datetime import datetime

def validator_datetime(v: datetime):
    return int(v.timestamp() * 1000) if v else None
