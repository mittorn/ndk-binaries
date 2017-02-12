# android-ndk-r10d with crystax ndk toolchain

This repo contains lightweight ndk.
It useful to setup ndk on Travis CI or tutorialspoint.com

### It does not contain:

 * LLVM/Clang toolchains
 * Tests
 * Third-party libraries that not needed for usual builds
 * 64-bit toolchains (unuseful for Xash3D projects)
 * Old gcc-4.6, 4.8 toolchains as 4.9 is stable enough

### Added:

 * gcc-6.2 toolchain from crystax ndk

### Changes was made:

 * All file duplicates are replaced with symlinks to keep disk space
 * crystax ndk binaries were patched to skip linking with -lcrystax. I just replaced -lcrystax with spaces in gcc and g++ binaries

