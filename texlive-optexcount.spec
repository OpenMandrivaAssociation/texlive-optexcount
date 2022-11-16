Name:		texlive-optexcount
Version:	59817
Release:	1
Summary:	Python script for counting words in OpTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/optexcount
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/optexcount.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/optexcount.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/optexcount.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
OpTeXcount is a basic python utility that analyzes OpTeX source
code. It is inspired by already existing TeXcount for LaTeX.
The functionality is really lightweight and basic. It counts
words and other elements of OpTeX document and sorts them out
into individual categories. Users can print the source code
with highlighted words using several colors,so they see what is
considered as word, header etc.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%doc %{_texmfdistdir}/texmf-dist/source/support/optexcount
%{_texmfdistdir}/texmf-dist/scripts/optexcount
%doc %{_texmfdistdir}/texmf-dist/doc/support/optexcount

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
