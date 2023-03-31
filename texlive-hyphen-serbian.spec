Name:		texlive-hyphen-serbian
Version:	58609
Release:	2
Summary:	Serbian hyphenation patterns
Group:		Publishing
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-serbian.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Serbian in T1/EC, T2A and UTF-8
encodings. For 8-bit engines the patterns are available
separately as 'serbian' in T1/EC encoding for Latin script and
'serbianc' in T2A encoding for Cyrillic script. Unicode engines
should only use 'serbian' which has patterns in both scripts
combined.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*
%_texmf_language_dat_d/hyphen-serbian
%_texmf_language_def_d/hyphen-serbian
%_texmf_language_lua_d/hyphen-serbian

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-serbian <<EOF
\%% from hyphen-serbian:
serbian loadhyph-sr-latn.tex
serbianc loadhyph-sr-cyrl.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-serbian
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-serbian <<EOF
\%% from hyphen-serbian:
\addlanguage{serbian}{loadhyph-sr-latn.tex}{}{2}{2}
\addlanguage{serbianc}{loadhyph-sr-cyrl.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-serbian
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-serbian <<EOF
-- from hyphen-serbian:
	['serbian'] = {
		loader = 'loadhyph-sr-latn.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-sh-latn.pat.txt,hyph-sh-cyrl.pat.txt',
		hyphenation = 'hyph-sh-latn.hyp.txt,hyph-sh-cyrl.hyp.txt',
	},
	['serbianc'] = {
		loader = 'loadhyph-sr-cyrl.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-sh-latn.pat.txt,hyph-sh-cyrl.pat.txt',
		hyphenation = 'hyph-sh-latn.hyp.txt,hyph-sh-cyrl.hyp.txt',
	},
EOF
