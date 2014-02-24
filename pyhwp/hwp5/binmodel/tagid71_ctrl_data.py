# -*- coding: utf-8 -*-
#
#   pyhwp : hwp file format parser in python
#   Copyright (C) 2010-2014 mete0r <mete0r@sarangbang.or.kr>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from hwp5.binmodel._shared import RecordModelType
from hwp5.binmodel._shared import RecordModel
from hwp5.tagids import HWPTAG_CTRL_DATA


control_data_models = dict()


class ControlDataType(RecordModelType):

    def __new__(mcs, name, bases, attrs):
        cls = RecordModelType.__new__(mcs, name, bases, attrs)
        if 'parent_model_type' in attrs:
            parent_model_type = attrs['parent_model_type']
            assert parent_model_type not in control_data_models
            control_data_models[parent_model_type] = cls
        return cls


class ControlData(RecordModel):
    __metaclass__ = ControlDataType
    tagid = HWPTAG_CTRL_DATA

    extension_types = control_data_models

    def get_extension_key(cls, context, model):
        ''' parent model type '''
        parent = context.get('parent')
        if parent:
            return parent[1]['type']
    get_extension_key = classmethod(get_extension_key)