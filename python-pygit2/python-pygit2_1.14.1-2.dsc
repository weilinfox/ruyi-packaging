-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

Format: 3.0 (quilt)
Source: python-pygit2
Binary: python3-pygit2, python-pygit2-doc
Architecture: any all
Version: 1.14.1-2
Maintainer: Debian Python Team <team+python@tracker.debian.org>
Uploaders: Ondřej Nový <onovy@debian.org>, Utkarsh Gupta <utkarsh@debian.org>, Timo Röhling <roehling@debian.org>,
Homepage: https://github.com/libgit2/pygit2
Description: Python bindings for libgit2
 The Pygit2 module provides a set of Python bindings to the libgit2 shared
 library. libgit2 implements the core of Git. Pygit2 works with Python 2.7,
 3.x and pypy.
Standards-Version: 4.6.2
Vcs-Browser: https://salsa.debian.org/python-team/packages/python-pygit2
Vcs-Git: https://salsa.debian.org/python-team/packages/python-pygit2.git
Testsuite: autopkgtest-pkg-pybuild
Build-Depends: debhelper-compat (= 13), dh-sequence-python3, dh-sequence-sphinxdoc, libffi-dev, libgit2-dev (>= 1.7), libgit2-dev (<< 1.8~), libpython3-all-dev, libpython3.11-dev, python3.11, python3-all-dev:any, python3-cffi:native (>= 1.6.0), python3-pycparser:native, python3-pytest <!nocheck>, python3-setuptools, python3-six, python3-sphinx-rtd-theme:native <!nodoc>, python3-sphinx:native <!nodoc>
Package-List:
 python-pygit2-doc deb doc optional arch=all
 python3-pygit2 deb python optional arch=any
Checksums-Sha1:
 c04d33e54571f64e1733804d29595b73d6837484 788770 python-pygit2_1.14.1.orig.tar.gz
 a985bfe4466793bf096c813e4b75ad5a1fbf780b 7396 python-pygit2_1.14.1-2.debian.tar.xz
Checksums-Sha256:
 2e60ee9ae0ccbf8f61d5ff29e59c8ac69a07b9be4ae44c5545f2cc35fe070b41 788770 python-pygit2_1.14.1.orig.tar.gz
 053a6c8671879476bd9a650718dbadfbefb8cbf668b85d1b2bf2d44460960e2b 7396 python-pygit2_1.14.1-2.debian.tar.xz
Files:
 b95c857956644757b7d322196a1a82aa 788770 python-pygit2_1.14.1.orig.tar.gz
 8e990ecec8e8dce166d45692eee16878 7396 python-pygit2_1.14.1-2.debian.tar.xz

-----BEGIN PGP SIGNATURE-----

iQHKBAEBCgA0FiEElqBGeGZZnZI7Q7Co2vHnpNQBu/MFAmbe6qkWHGNhaXdlaWxp
bkBpc2Nhcy5hYy5jbgAKCRDa8eek1AG78+EqDAC39lq6QMj2iiXqqFIhy1i9Cmjb
oXsCoEcpN5U4nG3x1FeqafH2jAEy6f0SVr4FKPxbuLLfRfdBK3jwJwWKnMuT7fPh
Y3IFZxerTvCxu37kUBKo/jsFs2DacfLkenxDuvpihVSvF4VS8Jux8L1Zf625pkbH
9SdS/IUKfPwNoww2O/r36Xs80Gj25p+K0EYyaJMrjePJf/3OTv2w0L/fQ9uilpAc
3ChEStw0TiyglYwG3idRNo/+t53Jm6Tof8vLwvkH50emlRJz1EBZQfWIkVgEL4jM
SZ+FKgWWfxHVq+RKkpJJXvjKvkOBwmn1iqWPMF+sUYLWfulwsxP2YgeYy0SLjwbc
OAL+y4woYkPQblKmALIXpSG7IvVtXLfusKTjzJylArF38fwbc/jbsExvbZXVBjZS
w9ARxwnvkQ5Xjn+FZZMcJdF3A3pPy7y2hW9JEhyy5QKSSzX27CZZXBn6GNSRQq04
GNopd4ytlgMVkPEL+AHKQAvf3OgOILdRWXVeJdA=
=WS9B
-----END PGP SIGNATURE-----
