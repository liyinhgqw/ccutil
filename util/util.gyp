{
  'target_defaults': {
    'include_dirs': [
      '..',
    ],
  },
  'targets': [
    {
      'target_name': 'util',
      'type': 'static_library',
      'sources': [
         'arena.cc',
         'arena.h',
      ],
    },
  ],
}
