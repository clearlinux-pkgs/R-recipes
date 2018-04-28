#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-recipes
Version  : 0.1.2
Release  : 6
URL      : https://cran.r-project.org/src/contrib/recipes_0.1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/recipes_0.1.2.tar.gz
Summary  : Preprocessing Tools to Create Design Matrices
Group    : Development/Tools
License  : GPL-2.0
Requires: R-DRR
Requires: R-RcppRoll
Requires: R-broom
Requires: R-ddalpha
Requires: R-dimRed
Requires: R-dplyr
Requires: R-fastICA
Requires: R-gower
Requires: R-ipred
Requires: R-psych
Requires: R-tidyr
Requires: R-tidyselect
Requires: R-timeDate
BuildRequires : R-DRR
BuildRequires : R-RcppRoll
BuildRequires : R-broom
BuildRequires : R-ddalpha
BuildRequires : R-dimRed
BuildRequires : R-dplyr
BuildRequires : R-fastICA
BuildRequires : R-gower
BuildRequires : R-ipred
BuildRequires : R-psych
BuildRequires : R-tidyr
BuildRequires : R-tidyselect
BuildRequires : R-timeDate
BuildRequires : clr-R-helpers

%description
design matrices. Recipes consist of one or more data manipulation 
    and analysis "steps". Statistical parameters for the steps can 
    be estimated from an initial data set and then applied to 
    other data sets. The resulting design matrices can then be used 
    as inputs into statistical or machine learning models.

%prep
%setup -q -c -n recipes

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521292306

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521292306
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library recipes
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library recipes
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library recipes
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library recipes|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/recipes/DESCRIPTION
/usr/lib64/R/library/recipes/INDEX
/usr/lib64/R/library/recipes/Meta/Rd.rds
/usr/lib64/R/library/recipes/Meta/data.rds
/usr/lib64/R/library/recipes/Meta/features.rds
/usr/lib64/R/library/recipes/Meta/hsearch.rds
/usr/lib64/R/library/recipes/Meta/links.rds
/usr/lib64/R/library/recipes/Meta/nsInfo.rds
/usr/lib64/R/library/recipes/Meta/package.rds
/usr/lib64/R/library/recipes/Meta/vignette.rds
/usr/lib64/R/library/recipes/NAMESPACE
/usr/lib64/R/library/recipes/NEWS.md
/usr/lib64/R/library/recipes/R/recipes
/usr/lib64/R/library/recipes/R/recipes.rdb
/usr/lib64/R/library/recipes/R/recipes.rdx
/usr/lib64/R/library/recipes/data/Rdata.rdb
/usr/lib64/R/library/recipes/data/Rdata.rds
/usr/lib64/R/library/recipes/data/Rdata.rdx
/usr/lib64/R/library/recipes/data/datalist
/usr/lib64/R/library/recipes/doc/Custom_Steps.R
/usr/lib64/R/library/recipes/doc/Custom_Steps.Rmd
/usr/lib64/R/library/recipes/doc/Custom_Steps.html
/usr/lib64/R/library/recipes/doc/Dummies.R
/usr/lib64/R/library/recipes/doc/Dummies.Rmd
/usr/lib64/R/library/recipes/doc/Dummies.html
/usr/lib64/R/library/recipes/doc/Ordering.Rmd
/usr/lib64/R/library/recipes/doc/Ordering.html
/usr/lib64/R/library/recipes/doc/Selecting_Variables.R
/usr/lib64/R/library/recipes/doc/Selecting_Variables.Rmd
/usr/lib64/R/library/recipes/doc/Selecting_Variables.html
/usr/lib64/R/library/recipes/doc/Simple_Example.R
/usr/lib64/R/library/recipes/doc/Simple_Example.Rmd
/usr/lib64/R/library/recipes/doc/Simple_Example.html
/usr/lib64/R/library/recipes/doc/Skipping.R
/usr/lib64/R/library/recipes/doc/Skipping.Rmd
/usr/lib64/R/library/recipes/doc/Skipping.html
/usr/lib64/R/library/recipes/doc/index.html
/usr/lib64/R/library/recipes/help/AnIndex
/usr/lib64/R/library/recipes/help/aliases.rds
/usr/lib64/R/library/recipes/help/paths.rds
/usr/lib64/R/library/recipes/help/recipes.rdb
/usr/lib64/R/library/recipes/help/recipes.rdx
/usr/lib64/R/library/recipes/html/00Index.html
/usr/lib64/R/library/recipes/html/R.css
