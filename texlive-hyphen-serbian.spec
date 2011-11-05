# revision 23092
# category TLCore
# catalog-ctan /language/hyphenation/srhyphc.tex
# catalog-date 2007-02-28 00:02:05 +0100
# catalog-license gpl
# catalog-version 1.0a
Name:		texlive-hyphen-serbian
Version:	1.0a
Release:	1
Summary:	Serbian hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hyphenation/srhyphc.tex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-serbian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8
Conflicts:	texlive-texmf <= 20110705-3

%description
Hyphenation patterns for Serbian in T1/EC, T2A and UTF-8
encodings. For 8-bit engines the patterns are available
separately as 'serbian' in T1/EC encoding for Latin script and
'serbianc' in T2A encoding for Cyrillic script. Unicode engines
should only use 'serbian' which has patterns in both scripts
combined.

%pre
    %_texmf_language_dat_pre
    %_texmf_language_def_pre
    %_texmf_language_lua_pre

%post
    %_texmf_language_dat_post
    %_texmf_language_def_post
    %_texmf_language_lua_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_pre
	%_texmf_language_def_pre
	%_texmf_language_lua_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_post
	%_texmf_language_def_post
	%_texmf_language_lua_post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-serbian
%_texmf_language_def_d/hyphen-serbian
%_texmf_language_lua_d/hyphen-serbian
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-serbian <<EOF
%% from hyphen-serbian:
serbian loadhyph-sr-latn.tex
serbianc loadhyph-sr-cyrl.tex
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-serbian <<EOF
%% from hyphen-serbian:
\addlanguage{serbian}{loadhyph-sr-latn.tex}{}{2}{2}
\addlanguage{serbianc}{loadhyph-sr-cyrl.tex}{}{2}{2}
EOF
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
