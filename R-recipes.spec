#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-recipes
Version  : 0.1.5
Release  : 20
URL      : https://cran.r-project.org/src/contrib/recipes_0.1.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/recipes_0.1.5.tar.gz
Summary  : Preprocessing Tools to Create Design Matrices
Group    : Development/Tools
License  : GPL-2.0
Requires: R-NMF
Requires: R-Rcpp
Requires: R-RcppRoll
Requires: R-ddalpha
Requires: R-dimRed
Requires: R-dplyr
Requires: R-fastICA
Requires: R-generics
Requires: R-gower
Requires: R-ipred
Requires: R-kernlab
Requires: R-lava
Requires: R-lubridate
Requires: R-pillar
Requires: R-pls
Requires: R-prodlim
Requires: R-tidyr
Requires: R-tidyselect
Requires: R-timeDate
BuildRequires : R-NMF
BuildRequires : R-Rcpp
BuildRequires : R-RcppRoll
BuildRequires : R-ddalpha
BuildRequires : R-dimRed
BuildRequires : R-dplyr
BuildRequires : R-fastICA
BuildRequires : R-generics
BuildRequires : R-gower
BuildRequires : R-ipred
BuildRequires : R-kernlab
BuildRequires : R-lava
BuildRequires : R-lubridate
BuildRequires : R-pillar
BuildRequires : R-pls
BuildRequires : R-prodlim
BuildRequires : R-tidyr
BuildRequires : R-tidyselect
BuildRequires : R-timeDate
BuildRequires : buildreq-R

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
export SOURCE_DATE_EPOCH=1553191915

%install
export SOURCE_DATE_EPOCH=1553191915
rm -rf %{buildroot}
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
R CMD check --no-manual --no-examples --no-codoc  recipes || :


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
/usr/lib64/R/library/recipes/doc/Roles.R
/usr/lib64/R/library/recipes/doc/Roles.Rmd
/usr/lib64/R/library/recipes/doc/Roles.html
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
/usr/lib64/R/library/recipes/tests/testthat.R
/usr/lib64/R/library/recipes/tests/testthat/test-update.R
/usr/lib64/R/library/recipes/tests/testthat/test_BoxCox.R
/usr/lib64/R/library/recipes/tests/testthat/test_YeoJohnson.R
/usr/lib64/R/library/recipes/tests/testthat/test_arrange.R
/usr/lib64/R/library/recipes/tests/testthat/test_bagimpute.R
/usr/lib64/R/library/recipes/tests/testthat/test_basics.R
/usr/lib64/R/library/recipes/tests/testthat/test_bin2factor.R
/usr/lib64/R/library/recipes/tests/testthat/test_bs.R
/usr/lib64/R/library/recipes/tests/testthat/test_center_scale.R
/usr/lib64/R/library/recipes/tests/testthat/test_classdist.R
/usr/lib64/R/library/recipes/tests/testthat/test_colcheck.R
/usr/lib64/R/library/recipes/tests/testthat/test_corr.R
/usr/lib64/R/library/recipes/tests/testthat/test_count.R
/usr/lib64/R/library/recipes/tests/testthat/test_data.frame.R
/usr/lib64/R/library/recipes/tests/testthat/test_date.R
/usr/lib64/R/library/recipes/tests/testthat/test_depth.R
/usr/lib64/R/library/recipes/tests/testthat/test_discretized.R
/usr/lib64/R/library/recipes/tests/testthat/test_downsample.R
/usr/lib64/R/library/recipes/tests/testthat/test_dummies.R
/usr/lib64/R/library/recipes/tests/testthat/test_factors2strings.R
/usr/lib64/R/library/recipes/tests/testthat/test_filter.R
/usr/lib64/R/library/recipes/tests/testthat/test_formula.R
/usr/lib64/R/library/recipes/tests/testthat/test_geodist.R
/usr/lib64/R/library/recipes/tests/testthat/test_grouped_df.R
/usr/lib64/R/library/recipes/tests/testthat/test_holiday.R
/usr/lib64/R/library/recipes/tests/testthat/test_hyperbolic.R
/usr/lib64/R/library/recipes/tests/testthat/test_ica.R
/usr/lib64/R/library/recipes/tests/testthat/test_integer.R
/usr/lib64/R/library/recipes/tests/testthat/test_interact.R
/usr/lib64/R/library/recipes/tests/testthat/test_intercept.R
/usr/lib64/R/library/recipes/tests/testthat/test_inverse.R
/usr/lib64/R/library/recipes/tests/testthat/test_invlogit.R
/usr/lib64/R/library/recipes/tests/testthat/test_isomap.R
/usr/lib64/R/library/recipes/tests/testthat/test_knnimpute.R
/usr/lib64/R/library/recipes/tests/testthat/test_kpca.R
/usr/lib64/R/library/recipes/tests/testthat/test_lag.R
/usr/lib64/R/library/recipes/tests/testthat/test_lincomb.R
/usr/lib64/R/library/recipes/tests/testthat/test_list_cols.R
/usr/lib64/R/library/recipes/tests/testthat/test_log.R
/usr/lib64/R/library/recipes/tests/testthat/test_logit.R
/usr/lib64/R/library/recipes/tests/testthat/test_lowerimpute.R
/usr/lib64/R/library/recipes/tests/testthat/test_matrix.R
/usr/lib64/R/library/recipes/tests/testthat/test_meanimpute.R
/usr/lib64/R/library/recipes/tests/testthat/test_medianimpute.R
/usr/lib64/R/library/recipes/tests/testthat/test_missing.R
/usr/lib64/R/library/recipes/tests/testthat/test_modeimpute.R
/usr/lib64/R/library/recipes/tests/testthat/test_multivariate.R
/usr/lib64/R/library/recipes/tests/testthat/test_mutate.R
/usr/lib64/R/library/recipes/tests/testthat/test_naomit.R
/usr/lib64/R/library/recipes/tests/testthat/test_nnmf.R
/usr/lib64/R/library/recipes/tests/testthat/test_nomial_types.R
/usr/lib64/R/library/recipes/tests/testthat/test_novel.R
/usr/lib64/R/library/recipes/tests/testthat/test_ns.R
/usr/lib64/R/library/recipes/tests/testthat/test_num2factor.R
/usr/lib64/R/library/recipes/tests/testthat/test_nzv.R
/usr/lib64/R/library/recipes/tests/testthat/test_ordinalscore.R
/usr/lib64/R/library/recipes/tests/testthat/test_other.R
/usr/lib64/R/library/recipes/tests/testthat/test_pca.R
/usr/lib64/R/library/recipes/tests/testthat/test_pls.R
/usr/lib64/R/library/recipes/tests/testthat/test_poly.R
/usr/lib64/R/library/recipes/tests/testthat/test_profile.R
/usr/lib64/R/library/recipes/tests/testthat/test_range.R
/usr/lib64/R/library/recipes/tests/testthat/test_range_check.R
/usr/lib64/R/library/recipes/tests/testthat/test_ratio.R
/usr/lib64/R/library/recipes/tests/testthat/test_regex.R
/usr/lib64/R/library/recipes/tests/testthat/test_relu.R
/usr/lib64/R/library/recipes/tests/testthat/test_retraining.R
/usr/lib64/R/library/recipes/tests/testthat/test_rm.R
/usr/lib64/R/library/recipes/tests/testthat/test_roles.R
/usr/lib64/R/library/recipes/tests/testthat/test_roll.R
/usr/lib64/R/library/recipes/tests/testthat/test_rollimpute.R
/usr/lib64/R/library/recipes/tests/testthat/test_sample.R
/usr/lib64/R/library/recipes/tests/testthat/test_select_terms.R
/usr/lib64/R/library/recipes/tests/testthat/test_shuffle.R
/usr/lib64/R/library/recipes/tests/testthat/test_skipping.R
/usr/lib64/R/library/recipes/tests/testthat/test_slice.R
/usr/lib64/R/library/recipes/tests/testthat/test_sparsity.R
/usr/lib64/R/library/recipes/tests/testthat/test_spatialsign.R
/usr/lib64/R/library/recipes/tests/testthat/test_sqrt.R
/usr/lib64/R/library/recipes/tests/testthat/test_string2factor.R
/usr/lib64/R/library/recipes/tests/testthat/test_stringsAsFactors.R
/usr/lib64/R/library/recipes/tests/testthat/test_term_info.R
/usr/lib64/R/library/recipes/tests/testthat/test_tidy.R
/usr/lib64/R/library/recipes/tests/testthat/test_unorder.R
/usr/lib64/R/library/recipes/tests/testthat/test_upsample.R
/usr/lib64/R/library/recipes/tests/testthat/test_zv.R
