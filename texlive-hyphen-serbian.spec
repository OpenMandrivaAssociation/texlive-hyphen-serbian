%global tl_name hyphen-serbian
%global tl_revision 78069
%global tl_version 1.0a

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Serbian hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hyphenation/srhyphc.tex
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-serbian.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Serbian in T1/EC, T2A and UTF-8 encodings. For
8-bit engines the patterns are available separately as 'serbian' in
T1/EC encoding for Latin script and 'serbianc' in T2A encoding for
Cyrillic script. Unicode engines should only use 'serbian' which has
patterns in both scripts combined.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-serbian:
serbian loadhyph-sr-latn.tex
serbianc loadhyph-sr-cyrl.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-serbian:
\addlanguage{serbian}{loadhyph-sr-latn.tex}{}{2}{2}
\addlanguage{serbianc}{loadhyph-sr-cyrl.tex}{}{2}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
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
TL_HYPHEN_EOF
