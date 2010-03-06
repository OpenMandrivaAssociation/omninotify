%define		_disable_ld_no_undefined	1

%define	name	omninotify
%define	libname	%mklibname %{name} 0
%define devname	%mklibname %{name} -d

Name:		%{name}
Version:	2.1
Release:	%mkrel 1
Group:		System/Servers
Summary:	Multi-threaded implementation of the CORBA Notification Service
License:	GPL
URL:		http://omninotify.sourceforge.net
Source0:	omniNotify-2.1.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	omniorb
BuildRequires:	omniorb-devel

Patch0:		long-long.patch
Patch1:		backward-iostream.patch
Patch2:		destdir.patch

%description
omniNotify is a multi-threaded implementation of the CORBA Notification
Service (CosNotification), a feature-enriched version of the CORBA Event
Service (CosEvents).omniNotify offers asynchronous, decoupled,
event-based communication between distributed and heterogeneous applications. 

omniNotify was developed by a group of researchers at AT&T Labs in
Florham Park, New Jersey.   Our  main design goal for omniNotify was
scalability: we wanted a service that scales well w.r.t. both number
of connected consumers and number (and complexity) of filters registered
by consumers.  To achieve this goal, the implementation exploits parallelism
during filter evaluation and dispatching of events to consumers. 

omniNotify is built on top of OmniORB, a free high performance C++ CORBA ORB
was developed by researchers at the lab which was originally the Olivetti
research lab (ORL), then the Olivetti/Oracle lab, and finally AT&T
Labs Cambridge.  It is now maintained by Duncan Grisby. omniNotify's good
performance is due in part to the excellent performance of OmniORB.

%files
%defattr(-,root,root)
%{_bindir}/notifd

#------------------------------------------------------------------------
%package	-n %{libname}
Summary:	%{name} shared libraries
Group:		System/Libraries
Provides:	lib%{name} = %{version}-%{release}

%description	-n %{libname}
This package provides %{name} shared libraries.

%files		-n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

#------------------------------------------------------------------------
%package	-n %{devname}
Summary:	%{name} shared libraries
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description	-n %{devname}
This package provides %{name} development files.

%files		-n %{devname}
%defattr(-,root,root)
%dir %{_includedir}/COS
%{_includedir}/COS/*
%dir %{_includedir}/omniNotify
%{_includedir}/omniNotify/*
%{_libdir}/*.so

#-----------------------------------------------------------------------
%prep
%setup -q -n omniNotify

%patch0 -p1
%patch1 -p1
%patch2 -p1

#-----------------------------------------------------------------------
%build
%configure --disable-static --enable-shared
%make

#-----------------------------------------------------------------------
%install
%makeinstall_std

#-----------------------------------------------------------------------
%clean
rm -rf %{buildroot}
