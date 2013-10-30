# `appnope`

Simple package for disabling App Nap on OS X 10.9,
which can be problematic.

Simply `import appnope`, and App Nap should be disabled.

It uses ctypes to wrap a `[NSProcessInfo beginActivityWithOptions]` call to disable App Nap.

To install, just:

    pip install appnope

or

    pip install -e git+https://github.com/minrk/appnope#egg=appnope
