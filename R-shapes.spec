%global packname  shapes
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.1_8
Release:          2
Summary:          Statistical shape analysis
Group:            Sciences/Mathematics
License:          GPL-2
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-8.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-scatterplot3d R-rgl R-MASS 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-scatterplot3d R-rgl R-MASS

%description
Routines for the statistical analysis of shapes. In particular, the
package provides routines for procrustes analysis, displaying shapes and
principal components, testing for mean shape difference, thin-plate spline
transformation grids and edge superimposition methods.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# FIXME (Error in rgl.open() : rgl.open failed)
%if 0
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help


%changelog
* Sat Feb 18 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1_5-1
+ Revision: 776927
- Import R-shapes
- Import R-shapes

