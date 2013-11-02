# -*- coding: utf-8 -*-

db.define_table('dict',
	Field('attr', 'text'))

db.define_table('picture',
	Field('path_to_file', 'text'),
	Field('picture', 'upload'))

db.define_table('picture_attributes',
	Field('picture', 'reference PICTURE'),
	Field('attr', 'reference DICT'))

db.define_table('post',
	Field('post_content', 'text'),
	Field('user_id', db.auth_user))
