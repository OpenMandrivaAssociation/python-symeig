%define tarname symeig

Summary: Symmetrical eigenvalue routines for numpy
Name: 	 python-%{tarname}
Version: 1.4.1
Release: 5
Source0: %{tarname}-%{version}.tar.lzma
License: LGPLv3+
Group: 	 Development/Python
Url: 	 https://mdp-toolkit.sourceforge.net/symeig.html
Requires: python >= 2.4, python-numpy
BuildRequires: lapack-devel
BuildRequires: python-devel >= 2.4
BuildRequires: python-numpy-devel >= 1.0

%description
The symeig module contains a Python wrapper for the LAPACK functions
that solve the standard and generalized eigenvalue problems for
symmetric (hermitian) positive definite matrices. Those specialized
algorithms provide an important speed-up relative to the generic
LAPACK eigenvalue problem solver in NumPy (linalg.eig and
linalg.eigh).

%prep
%setup -q -n %{tarname}-1.4

%build
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILELIST

%files -f FILELIST
%doc README COPY*



%changelog
* Tue Sep 15 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.4.1-3mdv2010.0
+ Revision: 442502
- rebuild

* Fri Jan 02 2009 Funda Wang <fundawang@mandriva.org> 1.4.1-2mdv2009.1
+ Revision: 323416
- rebuild

* Thu Oct 23 2008 Lev Givon <lev@mandriva.org> 1.4.1-1mdv2009.1
+ Revision: 296625
- Update to 1.4.1.

* Sun Oct 12 2008 Lev Givon <lev@mandriva.org> 1.4-1mdv2009.1
+ Revision: 292867
- import python-symeig


* Mon Jun 2 2008 Lev Givon <lev@mandriva.org> 1.4-1mdv2008.0
- Package for Mandriva.
