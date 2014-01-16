{
  'target_defaults': {
    'include_dirs': [
      '.',
    ],
  },
  'targets': [
    {
      'target_name': 'test',
      'type': 'executable',
      'dependencies': [
         'util/util.gyp:util',
      ],
      'sources': [
        'test/test.cc',
      ],
   },
  ],
}
