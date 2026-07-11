%global tl_name hyphen-serbian
%global tl_revision 78069

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0a
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
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Serbian in T1/EC, T2A and UTF-8 encodings. For
8-bit engines the patterns are available separately as 'serbian' in
T1/EC encoding for Latin script and 'serbianc' in T2A encoding for
Cyrillic script. Unicode engines should only use 'serbian' which has
patterns in both scripts combined.

