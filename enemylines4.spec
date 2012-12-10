Name:		enemylines4
Summary:	A simple futuristic racing game
Version:	1.0
Release:	10
Group:		Games/Arcade
License:	GPL+
URL:		http://proj.phk.at/el/4/
Source0:	http://proj.phk.at/el/4/%{name}-%{version}.tar.bz2
Source10:	%{name}.png
# include assert.h in track.cc to fix build failure - AdamW 2008/02
Patch0:		enemylines4-assert.patch
Patch1:		enemylines4-1.0-mdv-fix-gcc-4.3.patch
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(glut)
BuildRequires:	imagemagick

%description
A simple futuristic racing game. Urgent deliveries - Reach goal before
time runs out. Times aren't what they used to be though.
Road conditions are horrible and traffic safety and control systems
have been offline for months.

%prep
%setup -q
%patch0 -p1 -b .assert
%patch1 -p1 -b .gcc43

%build
%make

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/
cp ./data/* %{buildroot}%{_datadir}/%{name}/
install -m755 %{name} -D %{buildroot}%{_gamesbindir}/%{name}

mkdir -p %{buildroot}/%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
install -m644 %{SOURCE10} %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -scale 32x32 %{SOURCE10} %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16x16 %{SOURCE10} %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Categories=Game;ArcadeGame;
Name=Enemy Lines 4
Comment=A simple futuristic racing game
EOF

%files 
%doc README
%{_datadir}/%{name}
%{_gamesbindir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop

