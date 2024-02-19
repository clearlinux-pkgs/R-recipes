#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v4
# autospec commit: da8b975
#
Name     : R-recipes
Version  : 1.0.10
Release  : 75
URL      : https://cran.r-project.org/src/contrib/recipes_1.0.10.tar.gz
Source0  : https://cran.r-project.org/src/contrib/recipes_1.0.10.tar.gz
Summary  : Preprocessing and Feature Engineering Steps for Modeling
Group    : Development/Tools
License  : MIT
Requires: R-cli
Requires: R-clock
Requires: R-dplyr
Requires: R-ellipsis
Requires: R-generics
Requires: R-glue
Requires: R-gower
Requires: R-hardhat
Requires: R-ipred
Requires: R-lifecycle
Requires: R-lubridate
Requires: R-magrittr
Requires: R-purrr
Requires: R-rlang
Requires: R-tibble
Requires: R-tidyr
Requires: R-tidyselect
Requires: R-timeDate
Requires: R-vctrs
Requires: R-withr
BuildRequires : R-cli
BuildRequires : R-clock
BuildRequires : R-dplyr
BuildRequires : R-ellipsis
BuildRequires : R-generics
BuildRequires : R-glue
BuildRequires : R-gower
BuildRequires : R-hardhat
BuildRequires : R-ipred
BuildRequires : R-lifecycle
BuildRequires : R-lubridate
BuildRequires : R-magrittr
BuildRequires : R-purrr
BuildRequires : R-rlang
BuildRequires : R-tibble
BuildRequires : R-tidyr
BuildRequires : R-tidyselect
BuildRequires : R-timeDate
BuildRequires : R-vctrs
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
extensible framework for pipeable sequences of feature engineering
    steps provides preprocessing tools to be applied to data. Statistical
    parameters for the steps can be estimated from an initial data set and
    then applied to other data sets. The resulting processed output can
    then be used as inputs for statistical or machine learning models.

%prep
%setup -q -n recipes
pushd ..
cp -a recipes buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1708370893

%install
export SOURCE_DATE_EPOCH=1708370893
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/recipes/DESCRIPTION
/usr/lib64/R/library/recipes/INDEX
/usr/lib64/R/library/recipes/LICENSE
/usr/lib64/R/library/recipes/Meta/Rd.rds
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
/usr/lib64/R/library/recipes/boilerplate.R
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
/usr/lib64/R/library/recipes/doc/Skipping.R
/usr/lib64/R/library/recipes/doc/Skipping.Rmd
/usr/lib64/R/library/recipes/doc/Skipping.html
/usr/lib64/R/library/recipes/doc/index.html
/usr/lib64/R/library/recipes/doc/recipes.R
/usr/lib64/R/library/recipes/doc/recipes.Rmd
/usr/lib64/R/library/recipes/doc/recipes.html
/usr/lib64/R/library/recipes/help/AnIndex
/usr/lib64/R/library/recipes/help/aliases.rds
/usr/lib64/R/library/recipes/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/recipes/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/recipes/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/recipes/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/recipes/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/recipes/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/recipes/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/recipes/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/recipes/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/recipes/help/figures/logo.png
/usr/lib64/R/library/recipes/help/paths.rds
/usr/lib64/R/library/recipes/help/recipes.rdb
/usr/lib64/R/library/recipes/help/recipes.rdx
/usr/lib64/R/library/recipes/html/00Index.html
/usr/lib64/R/library/recipes/html/R.css
/usr/lib64/R/library/recipes/old-get_types.R
/usr/lib64/R/library/recipes/pls_test_references.R
/usr/lib64/R/library/recipes/tests/testthat.R
/usr/lib64/R/library/recipes/tests/testthat/_snaps/BoxCox.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/R4.2/discretize.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/R4.2/selections.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/R4.2/tidy.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/R4.3/discretize.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/R4.3/selections.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/YeoJohnson.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/arrange.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/basics.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/bin2factor.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/bs.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/case-weight-functions.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/center.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/class.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/classdist.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/classdist_shrunken.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/colcheck.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/corr.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/count.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/cut.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/date.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/depth.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/discretize.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/dummy.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/dummy_extract.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/dummy_multi_choice.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/extension_check.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/extract-dials.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/factor2string.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/filter.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/filter_missing.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/format.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/formula.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/geodist.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/harmonic.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/holiday.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/hyperbolic.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/ica.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/impute_bag.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/impute_knn.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/impute_linear.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/impute_lower.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/impute_mean.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/impute_median.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/impute_mode.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/impute_roll.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/indicate_na.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/integer.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/interact.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/intercept.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/inverse.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/invlogit.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/isomap.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/kpca.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/kpca_poly.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/kpca_rbf.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/lag.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/lincomb.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/log.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/logit.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/matrix.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/misc.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/missing.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/mutate.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/mutate_at.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/naomit.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/newvalues.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/nnmf_sparse.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/nomial_types.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/normalize.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/novel.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/ns.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/num2factor.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/nzv.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/ordinalscore.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/other.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/pca.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/percentile.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/pkg_check.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/pls.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/pls_old.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/poly.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/poly_bernstein.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/profile.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/range.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/range_check.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/ratio.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/regex.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/relevel.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/relu.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/rename.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/rename_at.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/retraining.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/rm.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/roles.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/sample.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/scale.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/select.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/selections.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/shuffle.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/skipping.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/slice.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/sparsity.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/spatialsign.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/spline_b.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/spline_convex.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/spline_monotone.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/spline_natural.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/spline_nonnegative.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/sqrt.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/string2factor.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/stringsAsFactors.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/tidy.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/time.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/unknown.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/unorder.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/update-role-requirements.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/update.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/window.md
/usr/lib64/R/library/recipes/tests/testthat/_snaps/zv.md
/usr/lib64/R/library/recipes/tests/testthat/helper-case-weights.R
/usr/lib64/R/library/recipes/tests/testthat/helper-extract_parameter_set.R
/usr/lib64/R/library/recipes/tests/testthat/old-get_types.RData
/usr/lib64/R/library/recipes/tests/testthat/print_test_output/tidy-select-trained
/usr/lib64/R/library/recipes/tests/testthat/print_test_output/tidy-select-untrained
/usr/lib64/R/library/recipes/tests/testthat/test-BoxCox.R
/usr/lib64/R/library/recipes/tests/testthat/test-YeoJohnson.R
/usr/lib64/R/library/recipes/tests/testthat/test-arrange.R
/usr/lib64/R/library/recipes/tests/testthat/test-bake.R
/usr/lib64/R/library/recipes/tests/testthat/test-basics.R
/usr/lib64/R/library/recipes/tests/testthat/test-bin2factor.R
/usr/lib64/R/library/recipes/tests/testthat/test-bs.R
/usr/lib64/R/library/recipes/tests/testthat/test-case-weight-functions.R
/usr/lib64/R/library/recipes/tests/testthat/test-center.R
/usr/lib64/R/library/recipes/tests/testthat/test-class.R
/usr/lib64/R/library/recipes/tests/testthat/test-classdist.R
/usr/lib64/R/library/recipes/tests/testthat/test-classdist_shrunken.R
/usr/lib64/R/library/recipes/tests/testthat/test-colcheck.R
/usr/lib64/R/library/recipes/tests/testthat/test-column_order.R
/usr/lib64/R/library/recipes/tests/testthat/test-corr.R
/usr/lib64/R/library/recipes/tests/testthat/test-count.R
/usr/lib64/R/library/recipes/tests/testthat/test-cut.R
/usr/lib64/R/library/recipes/tests/testthat/test-data.frame.R
/usr/lib64/R/library/recipes/tests/testthat/test-date.R
/usr/lib64/R/library/recipes/tests/testthat/test-depth.R
/usr/lib64/R/library/recipes/tests/testthat/test-discretize.R
/usr/lib64/R/library/recipes/tests/testthat/test-dummy.R
/usr/lib64/R/library/recipes/tests/testthat/test-dummy_extract.R
/usr/lib64/R/library/recipes/tests/testthat/test-dummy_multi_choice.R
/usr/lib64/R/library/recipes/tests/testthat/test-extension_check.R
/usr/lib64/R/library/recipes/tests/testthat/test-extract-dials.R
/usr/lib64/R/library/recipes/tests/testthat/test-factor2string.R
/usr/lib64/R/library/recipes/tests/testthat/test-filter.R
/usr/lib64/R/library/recipes/tests/testthat/test-filter_missing.R
/usr/lib64/R/library/recipes/tests/testthat/test-format.R
/usr/lib64/R/library/recipes/tests/testthat/test-formula.R
/usr/lib64/R/library/recipes/tests/testthat/test-geodist.R
/usr/lib64/R/library/recipes/tests/testthat/test-grouped_df.R
/usr/lib64/R/library/recipes/tests/testthat/test-harmonic.R
/usr/lib64/R/library/recipes/tests/testthat/test-holiday.R
/usr/lib64/R/library/recipes/tests/testthat/test-hyperbolic.R
/usr/lib64/R/library/recipes/tests/testthat/test-ica.R
/usr/lib64/R/library/recipes/tests/testthat/test-impute_bag.R
/usr/lib64/R/library/recipes/tests/testthat/test-impute_knn.R
/usr/lib64/R/library/recipes/tests/testthat/test-impute_linear.R
/usr/lib64/R/library/recipes/tests/testthat/test-impute_lower.R
/usr/lib64/R/library/recipes/tests/testthat/test-impute_mean.R
/usr/lib64/R/library/recipes/tests/testthat/test-impute_median.R
/usr/lib64/R/library/recipes/tests/testthat/test-impute_mode.R
/usr/lib64/R/library/recipes/tests/testthat/test-impute_roll.R
/usr/lib64/R/library/recipes/tests/testthat/test-indicate_na.R
/usr/lib64/R/library/recipes/tests/testthat/test-integer.R
/usr/lib64/R/library/recipes/tests/testthat/test-interact.R
/usr/lib64/R/library/recipes/tests/testthat/test-intercept.R
/usr/lib64/R/library/recipes/tests/testthat/test-inverse.R
/usr/lib64/R/library/recipes/tests/testthat/test-invlogit.R
/usr/lib64/R/library/recipes/tests/testthat/test-isomap.R
/usr/lib64/R/library/recipes/tests/testthat/test-kpca.R
/usr/lib64/R/library/recipes/tests/testthat/test-kpca_poly.R
/usr/lib64/R/library/recipes/tests/testthat/test-kpca_rbf.R
/usr/lib64/R/library/recipes/tests/testthat/test-lag.R
/usr/lib64/R/library/recipes/tests/testthat/test-lincomb.R
/usr/lib64/R/library/recipes/tests/testthat/test-list_cols.R
/usr/lib64/R/library/recipes/tests/testthat/test-log.R
/usr/lib64/R/library/recipes/tests/testthat/test-logit.R
/usr/lib64/R/library/recipes/tests/testthat/test-matrix.R
/usr/lib64/R/library/recipes/tests/testthat/test-misc.R
/usr/lib64/R/library/recipes/tests/testthat/test-missing.R
/usr/lib64/R/library/recipes/tests/testthat/test-multivariate.R
/usr/lib64/R/library/recipes/tests/testthat/test-mutate.R
/usr/lib64/R/library/recipes/tests/testthat/test-mutate_at.R
/usr/lib64/R/library/recipes/tests/testthat/test-naomit.R
/usr/lib64/R/library/recipes/tests/testthat/test-newvalues.R
/usr/lib64/R/library/recipes/tests/testthat/test-nnmf_sparse.R
/usr/lib64/R/library/recipes/tests/testthat/test-nomial_types.R
/usr/lib64/R/library/recipes/tests/testthat/test-normalize.R
/usr/lib64/R/library/recipes/tests/testthat/test-novel.R
/usr/lib64/R/library/recipes/tests/testthat/test-ns.R
/usr/lib64/R/library/recipes/tests/testthat/test-num2factor.R
/usr/lib64/R/library/recipes/tests/testthat/test-nzv.R
/usr/lib64/R/library/recipes/tests/testthat/test-ordinalscore.R
/usr/lib64/R/library/recipes/tests/testthat/test-other.R
/usr/lib64/R/library/recipes/tests/testthat/test-pca.R
/usr/lib64/R/library/recipes/tests/testthat/test-percentile.R
/usr/lib64/R/library/recipes/tests/testthat/test-pkg_check.R
/usr/lib64/R/library/recipes/tests/testthat/test-pls.R
/usr/lib64/R/library/recipes/tests/testthat/test-pls_old.R
/usr/lib64/R/library/recipes/tests/testthat/test-poly.R
/usr/lib64/R/library/recipes/tests/testthat/test-poly_bernstein.R
/usr/lib64/R/library/recipes/tests/testthat/test-prepper.R
/usr/lib64/R/library/recipes/tests/testthat/test-profile.R
/usr/lib64/R/library/recipes/tests/testthat/test-range.R
/usr/lib64/R/library/recipes/tests/testthat/test-range_check.R
/usr/lib64/R/library/recipes/tests/testthat/test-ratio.R
/usr/lib64/R/library/recipes/tests/testthat/test-regex.R
/usr/lib64/R/library/recipes/tests/testthat/test-relevel.R
/usr/lib64/R/library/recipes/tests/testthat/test-relu.R
/usr/lib64/R/library/recipes/tests/testthat/test-rename.R
/usr/lib64/R/library/recipes/tests/testthat/test-rename_at.R
/usr/lib64/R/library/recipes/tests/testthat/test-retraining.R
/usr/lib64/R/library/recipes/tests/testthat/test-rm.R
/usr/lib64/R/library/recipes/tests/testthat/test-roles.R
/usr/lib64/R/library/recipes/tests/testthat/test-sample.R
/usr/lib64/R/library/recipes/tests/testthat/test-scale.R
/usr/lib64/R/library/recipes/tests/testthat/test-select.R
/usr/lib64/R/library/recipes/tests/testthat/test-selections.R
/usr/lib64/R/library/recipes/tests/testthat/test-shuffle.R
/usr/lib64/R/library/recipes/tests/testthat/test-skipping.R
/usr/lib64/R/library/recipes/tests/testthat/test-slice.R
/usr/lib64/R/library/recipes/tests/testthat/test-sparsity.R
/usr/lib64/R/library/recipes/tests/testthat/test-spatialsign.R
/usr/lib64/R/library/recipes/tests/testthat/test-spline_b.R
/usr/lib64/R/library/recipes/tests/testthat/test-spline_convex.R
/usr/lib64/R/library/recipes/tests/testthat/test-spline_monotone.R
/usr/lib64/R/library/recipes/tests/testthat/test-spline_natural.R
/usr/lib64/R/library/recipes/tests/testthat/test-spline_nonnegative.R
/usr/lib64/R/library/recipes/tests/testthat/test-sqrt.R
/usr/lib64/R/library/recipes/tests/testthat/test-string2factor.R
/usr/lib64/R/library/recipes/tests/testthat/test-stringsAsFactors.R
/usr/lib64/R/library/recipes/tests/testthat/test-term_info.R
/usr/lib64/R/library/recipes/tests/testthat/test-tidy.R
/usr/lib64/R/library/recipes/tests/testthat/test-time.R
/usr/lib64/R/library/recipes/tests/testthat/test-unknown.R
/usr/lib64/R/library/recipes/tests/testthat/test-unorder.R
/usr/lib64/R/library/recipes/tests/testthat/test-update-role-requirements.R
/usr/lib64/R/library/recipes/tests/testthat/test-update.R
/usr/lib64/R/library/recipes/tests/testthat/test-window.R
/usr/lib64/R/library/recipes/tests/testthat/test-zv.R
/usr/lib64/R/library/recipes/tests/testthat/test_pls_new.RData
/usr/lib64/R/library/recipes/tests/testthat/test_pls_old.RData
