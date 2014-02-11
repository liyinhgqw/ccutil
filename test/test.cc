/*
 * test.cc
 *
 *  Created on: Jan 16, 2014
 *      Author: liyinhgqw
 */

#include "util/arena.h"
#include "util/status.h"
#include "util/testharness.h"
#include <stdio.h>

using namespace cc;

int main(int argc, char* argv[]) {
  Arena arena;
  arena.Allocate(1);
  printf("%lu \n", arena.MemoryUsage());

  arena.AllocateAligned(2);
  printf("%lu \n", arena.MemoryUsage());

  return 0;
}


