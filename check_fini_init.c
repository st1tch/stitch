#include <stdio.h>

static void init ()
{
  printf ("init_array\n");
}

static void (*const init_array []) ()
  __attribute__ ((section (".init_array"), aligned (sizeof (void *))))
  = { init };

static void fini ()
{
  printf ("fini_array\n");
}

static void (*const fini_array []) ()
  __attribute__ ((section (".fini_array"), aligned (sizeof (void *))))
  = { fini };

//-------------------------------------------------------------------------

static void ctor ()
{
  printf ("ctor\n");
}

static void (*const ctors []) ()
  __attribute__ ((section (".ctors"), aligned (sizeof (void *))))
  = { ctor };

static void dtor ()
{
  printf ("dtor\n");
}

static void (*const dtors []) ()
  __attribute__ ((section (".dtors"), aligned (sizeof (void *))))
  = { dtor };

//----------------------------------------------------------------------
int main ()
{
  printf ("main\n");
}
