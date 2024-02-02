<!DOCTYPE html>
<html lang="en">

<head>
    <script src="/js/core/jquery.min.js"></script>
    <meta charset="utf-8"/>
    <meta name="csrf-token" content="">

    <link rel="manifest" href="/manifest.json">

    <link rel="apple-touch-icon" sizes="76x76" href="/favicon.ico">
    <link rel="icon" type="image/png" href="/favicon.ico">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>

    
    <title>404 Page Not Found | Exploit Database</title>

    <meta name="description" content="Exploit Database 404" />


    <link rel="alternate" type="application/rss+xml" title="Exploit-DB.com RSS Feed" href="/rss.xml">

    <meta
            content='width=device-width, initial-scale=1.0, shrink-to-fit=no'
            name='viewport'/>

    <meta property="og:title" content="OffSec&#8217;s Exploit Database Archive">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://www.exploit-db.com/">

    <meta name="theme-color" content="#ec5e10">

    <script id="Cookiebot" src="https://consent.cookiebot.com/uc.js" data-cbid="5cfe7093-608f-4f4e-80b4-925b1e9d949f"
            data-georegions="{'region':'US-06','cbid':'6abbf59f-78fd-4d8f-ac7e-b57c0f046bbf'}" data-blockingmode="auto"
            type="text/javascript">
    </script>

    <script type="text/javascript">
        window.ga=window.ga||function(){(ga.q=ga.q||[]).push(arguments)};ga.l=+new Date;
        ga('create', 'UA-1981501-4', { 'cookieDomain': 'www.exploit-db.com' } );

        ga('send', 'pageview');
    </script>
    <script async src="https://www.google-analytics.com/analytics.js"
            type="text/javascript">

    </script>

    <!-- Material Design Icons https://materialdesignicons.com/ -->
    <link href="/css/materialdesignicons.min.css" media="all" rel="stylesheet" type="text/css"/>

    <!-- Theme CSS Files -->
    <link href="/css/bootstrap.min.css" rel="stylesheet"/>

    <link href="/css/now-ui-dashboard.css" rel="stylesheet"/>

    <link href="/css/app.css" rel="stylesheet"/>

    <style>
        .rbtn {
            border: 2px solid white;
            border-radius: 20px;
            color: black;
            padding: 8px;
            cursor: pointer;
        }

        .rsuccess {
            border-color: white;
            color: white;
        }

        .rsuccess:hover {
            background-color: white;
            color: #165283;
        }
        .rprimary {
            border-color: #ca4f0c;
            color: #ca4f0c;
        }

        .rprimary:hover {
            background-color: #ca4f0c;
            color: white;
        }
    </style>
</head>

<body class=" sidebar-mini">

<div class="wrapper">

    
    <div class="sidebar" data-color="orange">

    <div class="logo">

        
        <a href="/" class="simple-text logo-mini">
            &nbsp;<img src="/images/spider-white.png" alt="Exploit Database">
        </a>

        
        
            <a href="/" class="simple-text logo-normal">
                Exploit Database
            </a>

        
    </div>

    <div class="sidebar-wrapper">

        <ul class="nav">

            
            <li class="">

                <a href="/">
                    <i class="mdi mdi-ladybug mdi-24px"></i>
                    <p>Exploits</p>
                </a>

            </li>

            
            <li class="">

                <a href="/google-hacking-database">
                    <i class="mdi mdi-search-web mdi-24px"></i>
                    <p title="Google Hacking Database">GHDB</p>
                </a>

            </li>

            
            <li class="">

                <a href="/papers">
                    <i class="mdi mdi-file-outline mdi-24px"></i>
                    <p>Papers</p>
                </a>

            </li>

            
            <li class="">

                <a href="/shellcodes">
                    <i class="mdi mdi-chip mdi-24px"></i>
                    <p>Shellcodes</p>
                </a>

            </li>

        </ul>

        <hr/>

        <ul class="nav">



                <li>

                    <a class="nav-link" href="/search">
                        <i class="mdi mdi-database-search mdi-24px"></i>
                        <p title="Search Exploit-Database">Search EDB</p>
                    </a>

                </li>



            <li>

                
                <a class="nav-link" href="/searchsploit">
                    <i class="mdi mdi-book-open-page-variant mdi-24px"></i>
                    <p>SearchSploit Manual</p>
                </a>

            </li>

            <li>

                
                <a class="nav-link" href="/submit">
                    <i class="mdi mdi-upload mdi-24px"></i>
                    <p>Submissions</p>
                </a>

            </li>

        </ul>

        <hr/>

        <ul class="nav">

            <li>

                <a class="nav-link" href="https://www.offsec.com/">
                    <i class="mdi mdi-school mdi-24px"></i>
                    <p title="OffSec">Online Training </p>
                </a>

            </li>

<!--
            <li>

                <a class="nav-link" href="#" data-toggle="modal" data-target="#osresources">
                    <i class="mdi mdi-link-variant mdi-24px"></i>
                    <p>OffSec Resources</p>
                </a>

            </li>
-->
        </ul>

    </div>

</div>

    <div class="main-panel">

        
        <nav class="navbar navbar-expand-lg navbar-transparent  navbar-absolute
  bg-primary">

    <div class="container-fluid">

        <div class="navbar-wrapper">

            <div class="navbar-toggle">
                <button type="button" class="navbar-toggler" aria-label="Toggle Navigation">
                    <span class="navbar-toggler-bar bar1"></span>
                    <span class="navbar-toggler-bar bar2"></span>
                    <span class="navbar-toggler-bar bar3"></span>
                </button>
            </div>

            
            <a class="navbar-brand" href="/">
                <img src="/images/edb-logo.png" height="60" alt="Exploit Database">
            </a>

        </div>

        
        <div class="collapse navbar-collapse justify-content-end" id="navigation">

            <ul class="navbar-nav">

                
                    

                        
                           
                           

                            
                            
                                
                            
                        

                        

                            
                                
                            

                            
                               
                                                     
                                
                            

                            
                                
                            

                        
                    
                

                
                    

                        
                            
                            
                                
                            
                        

                    
                

                <li class="nav-item">

                    
                    <a class="nav-link" href="/exploit-database-statistics" aria-label="Exploit Database Statistics">
                        <i class="mdi mdi-chart-bar-stacked mdi-24px"></i>
                        <p>
                            <span class="d-lg-none d-md-block">Stats</span>
                        </p>
                    </a>

                </li>

                <li class="nav-item dropdown">

                    
                    <a class="nav-link dropdown-toggle" href="/"
                       id="navbarDropdownMenuLink" data-toggle="dropdown"
                       aria-haspopup="true" aria-expanded="false" aria-label="Site Information">

                        <i class="mdi mdi-information-outline mdi-24px"></i>
                        <p>
                            <span class="d-lg-none d-md-block">About Us</span>
                        </p>
                    </a>

                    <div class="dropdown-menu dropdown-menu-right"
                         aria-labelledby="navbarDropdownMenuLink">

                        <!-- <a class="dropdown-item" href="#" data-toggle="modal" data-target="#about" aria-label="About Exploit-DB"> -->
                        <a class="dropdown-item" href="/about-exploit-db" aria-label="About Exploit-DB">
                            About Exploit-DB
                        </a>

                        <a class="dropdown-item" href="/history" aria-label="Exploit-DB History">
                            Exploit-DB History
                        </a>

                        <a class="dropdown-item" href="/faq" aria-label="FAQ">
                            FAQ
                        </a>

                    </div>

                </li>

                
                                    <li class="nav-item">

                        <a class="nav-link" href="#" data-toggle="modal" data-target="#search" aria-label="Search Exploit-DB">
                            <i class="mdi mdi-database-search mdi-24px"></i>
                            <p>
                                <span class="d-lg-none d-md-block">Search</span>
                            </p>
                        </a>

                    </li>

                
            </ul>

        </div>

    </div>

</nav>

        
        
    <div class="panel-header panel-header-sm"></div>

    <div class="content">

        <div class="row">

            <div class="col-sm-10 col-md-8 offset-md-2 text-center">

                <div class="card card-contributions">

                    <div class="card-body ">

                        <h1 class="card-title">
                            404
                        </h1>

                        <h2 class="card-category">
                            Page Not Found
                        </h2>

                        <p>
                            The page you are looking for could not be found.
                        </p>

                    </div>

                    <hr>

                    <div class="card-footer">

                        <div class="card card-plain card-subcategories">

                            <div class="card-body">

                                <ul class="nav nav-pills nav-pills-primary nav-pills-icons justify-content-center
                                nav-fill">

                                    <li class="nav-item">

                                        <a class="nav-link" href="/">
                                            <i class="mdi mdi-ladybug mdi-24px"></i>
                                            Home
                                        </a>

                                    </li>

                                    <li class="nav-item">

                                        <a class="nav-link" href="/google-hacking-database">
                                            <i class="mdi mdi-search-web mdi-24px"></i>
                                            GHDB
                                        </a>

                                    </li>

                                    <li class="nav-item">

                                        <a class="nav-link" href="/papers">
                                            <i class="mdi mdi-file-outline mdi-24px"></i>
                                            Papers
                                        </a>

                                    </li>

                                    <li class="nav-item">

                                        <a class="nav-link" href="/shellcodes">
                                            <i class="mdi mdi-chip mdi-24px"></i>
                                            Shellcodes
                                        </a>

                                    </li>

                                </ul>

                            </div>

                        </div>

                    </div>

                </div>

            </div>

        </div>

    </div>


        
        <footer class="footer">

    <div class="container-fluid">

        <nav>

            <ul>

                <li>
                    <a href="https://twitter.com/exploitdb" target="_blank" aria-label="Exploit-DB Twitter" rel="noopener">

    <i class="mdi mdi-twitter mdi-36px"></i>
</a>


<a href="https://www.facebook.com/ExploitDB" target="_blank" aria-label="Exploit-DB Facebook" rel="noopener">

    <i class="mdi mdi-facebook mdi-36px"></i>
</a>


<a href="https://gitlab.com/exploit-database/exploitdb" target="_blank" aria-label="Exploit-DB GitLab" rel="noopener">

    <i class="mdi mdi-gitlab mdi-36px"></i>
</a>


<a href="/rss.xml" target="_blank" aria-label="Exploit-DB RSS" rel="noopener">

    <i class="mdi mdi-rss mdi-36px"></i>
</a>
                </li>

                <li>

                    <a href="/">
                        Exploit Database by OffSec
                    </a>

                </li>

                <li>

                    <a href="/terms">
                        Terms
                    </a>

                </li>

                <li>

                    <a href="/privacy">
                        Privacy
                    </a>

                </li>

                <li>

                    <!-- <a href="#" data-toggle="modal" data-target="#about"> -->
                        <a href="/about-exploit-db">
                        About Us
                    </a>

                </li>

                <li>

                    <a href="/faq">
                        FAQ
                    </a>

                </li>

                <li>

                    <a href="/cookies">
                        Cookies
                    </a>

                </li>

            </ul>

        </nav>

        <div class="copyright mt-4">

            &copy;
            <a href="https://www.offsec.com/" target="_blank">OffSec Services Limited</a> 2024. All rights reserved.

        </div>

    </div>

    <!-- About EDB/GHDB Modal -->
<div class="modal fade bd-example-modal-lg" id="about" tabindex="-1"
     role="dialog" aria-labelledby="searchModalTitle" aria-hidden="true">

    <div class="modal-dialog modal-dialog-centered modal-dialog modal-lg"
         role="document">

        <div class="modal-content">

            <div class="modal-header">

                <h5 class="modal-title"
                    id="aboutModalTitle">About The Exploit Database
                </h5>

                <button type="button" class="close" data-dismiss="modal"
                        aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>

            </div>

            <div class="modal-body">

                <div class="row">

                    <p>
                        <a href="https://www.offsec.com/" target="_blank" rel="noopener">
                            <img class="float-left" src="/images/offsec-logo.png"
                                 alt="OffSec">
                        </a>
                        The Exploit Database is maintained by <a
                                href="https://www.offsec.com/community-projects/"
                                target="_blank" rel="noopener">OffSec</a>, an information security training company
                        that provides various <a
                                href="https://www.offsec.com/courses-and-certifications/"
                                target="_blank" rel="noopener">Information Security Certifications</a> as well as high end <a
                                href="https://www.offsec.com/penetration-testing/"
                                target="_blank" rel="noopener">penetration testing</a> services. The Exploit Database is a
                        non-profit project that is provided as a public service by OffSec.
                    </p>

                    <p>The Exploit Database is a <a
                                href="http://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html" target="_blank" rel="noopener">CVE
                            compliant</a> archive of public exploits and corresponding vulnerable software,
                        developed for use by penetration testers and vulnerability researchers. Our aim is to serve
                        the most comprehensive collection of exploits gathered through direct submissions, mailing
                        lists, as well as other public sources, and present them in a freely-available and
                        easy-to-navigate database. The Exploit Database is a repository for exploits and
                        proof-of-concepts rather than advisories, making it a valuable resource for those who need
                        actionable data right away.
                    </p>

                    <p>The <a href="/google-hacking-database">Google Hacking Database (GHDB)</a>
                        is a categorized index of Internet search engine queries designed to uncover interesting,
                        and usually sensitive, information made publicly available on the Internet. In most cases,
                        this information was never meant to be made public but due to any number of factors this
                        information was linked in a web document that was crawled by a search engine that
                        subsequently followed that link and indexed the sensitive information.
                    </p>

                    <p>The process known as “Google Hacking” was popularized in 2000 by Johnny
                        Long, a professional hacker, who began cataloging these queries in a database known as the
                        Google Hacking Database. His initial efforts were amplified by countless hours of community
                        member effort, documented in the book Google Hacking For Penetration Testers and popularised
                        by a barrage of media attention and Johnny’s talks on the subject such as this early talk
                        recorded at <a href="https://www.defcon.org/html/links/dc-archives/dc-13-archive.html"
                                       target="_blank" rel="noopener">DEFCON 13</a>. Johnny coined the term “Googledork” to refer
                        to “a foolish or inept person as revealed by Google“. This was meant to draw attention to
                        the fact that this was not a “Google problem” but rather the result of an often
                        unintentional misconfiguration on the part of a user or a program installed by the user.
                        Over time, the term “dork” became shorthand for a search query that located sensitive
                        information and “dorks” were included with may web application vulnerability releases to
                        show examples of vulnerable web sites.
                    </p>

                    <p>
                        After nearly a decade of hard work by the community, Johnny turned the GHDB
                        over to <a
                                href="https://www.offsec.com/community-projects/"
                                target="_blank" rel="noopener">OffSec</a> in November 2010, and it is now maintained as
                        an extension of the <a href="/">Exploit Database</a>. Today, the GHDB includes searches for
                        other online search engines such as <a href="https://www.bing.com/" target="_blank" rel="noopener">Bing</a>,
                        and other online repositories like <a href="https://github.com/" target="_blank" rel="noopener">GitHub</a>,
                        producing different, yet equally valuable results.
                    </p>


                </div>

            </div>

            <div class="modal-footer">

                <button type="button"
                        class="btn btn-primary"
                        data-dismiss="modal">Close
                </button>

            </div>

        </div>

    </div>

</div>


    <div class="modal fade bd-example-modal-lg" id="osresources" tabindex="-1"
     role="dialog" aria-labelledby="searchModalTitle" aria-hidden="true">

    <div class="modal-dialog modal-dialog-centered modal-dialog modal-lg"
         role="document">

        <div class="modal-content">

            <div class="modal-header">

                <h5 class="modal-title text-primary"
                    id="resourcesModalTitle">OffSec Resources
                </h5>

                <button type="button" class="close" data-dismiss="modal"
                        aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>

            </div>

            <div class="modal-body">

                <table class="table dataTable table-borderless">

                            <thead>

                            <!-- marker #3 -->
                            <tr>
                                <th>
                                    <strong>Databases</strong>
                                </th>
                                <th>
                                    <strong>Links</strong>
                                </th>
                                <th>
                                    <strong>Sites</strong>
                                </th>
                                <th>
                                    <strong>Solutions</strong>
                                </th>
                            </tr>

                            </thead>

                            <tbody>

                            <tr class="text-center">
                                <td>
                                    <a href="/">
                                        Exploits
                                    </a>
                                </td>
                                <td>
                                    <a href="/search">
                                        Search Exploit-DB
                                    </a>
                                </td>
                                <td>
                                    <a href="https://www.offsec.com/"
                                       target="_blank" rel="noopener">
                                        OffSec
                                    </a>
                                </td>
                                <td>
                                    <a href="https://www.offsec.com/courses-and-certifications/"
                                       target="_blank" rel="noopener">Courses and Certifications
                                    </a>
                                </td>
                            </tr>

                            <tr class="text-center">
                                <td>
                                    <a href="/google-hacking-database">
                                        Google Hacking
                                    </a>
                                </td>
                                <td>
                                    <a href="/submit">
                                        Submit Entry
                                    </a>
                                </td>
                                <td>
                                    <a href="https://www.kali.org/"
                                       target="_blank" rel="noopener">
                                        Kali Linux
                                    </a>
                                </td>
                                <td>
                                    <a href="https://www.offsec.com/learn/"
                                       target="_blank" rel="noopener">Learn Subscriptions
                                    </a>

                                </td>
                            </tr>

                            <tr class="text-center">
                                <td>
                                    <a href="/papers">
                                        Papers
                                    </a>
                                </td>
                                <td>
                                    <a href="/serchsploit">
                                        SearchSploit Manual
                                    </a>
                                </td>
                                <td>
                                    <a href="https://www.vulnhub.com/"
                                       target="_blank" rel="noopener">VulnHub
                                    </a>
                                </td>
                                <td>
                                    <a href="https://www.offsec.com/cyber-range/"
                                       target="_blank" rel="noopener">OffSec Cyber Range
                                    </a>
                                </td>
                            </tr>

                            <tr class="text-center">
                                <td></td>
                                <td>
                                    <a href="https://www.offsec.com/labs/"
                                       target="_blank" rel="noopener">Proving Grounds
                                    </a>
                                </td>
                            </tr>

                            <tr class="text-center">
                                <td>
                                    <a href="/shellcodes">
                                        Shellcodes
                                    </a>
                                </td>
                                <td>
                                    <a href="/serchsploit">
                                        Exploit Statistics
                                    </a>
                                </td>
                                <td></td>
                                <td>
                                    <a href="https://www.offsec.com/labs/"
                                       target="_blank" rel="noopener">Proving Grounds
                                    </a>
                                </td>
                            </tr>
                            <tr>
                                <td></td>
                                <td></td>
                                <td></td>
                                <td>
                                    <a href="https://www.offsec.com/penetration-testing/"
                                       target="_blank" rel="noopener">Penetration Testing Services
                                    </a>
                                </td>
                            </tr>

                            </tbody>

                        </table>

            </div>

            <div class="modal-footer">

                <button type="button"
                        class="btn btn-primary"
                        data-dismiss="modal">Close
                </button>

            </div>

        </div>

    </div>

</div>

    <!-- Advanced Search Modal -->
<div class="modal fade bd-example-modal-lg" id="search" tabindex="-1"
     role="dialog" aria-labelledby="searchModalTitle" aria-hidden="true">

    <div class="modal-dialog modal-dialog-centered modal-dialog modal-lg"
         role="document">

        <div class="modal-content">

            <div class="modal-header">

                <h5 class="modal-title"
                    id="searchModalTitle">Search The Exploit Database
                </h5>

                <button type="button" class="close" data-dismiss="modal"
                        aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>

            </div>

            <div class="modal-body">

                <form action="https://www.exploit-db.com/search" method="GET" id="searchForm">

                    <div class="row">

                        <div class="col-sm-12 col-lg-8">

                            <div class="form-group">

                                <label for="titleSearch" class="control-label text-primary">Title</label>

                                <input id="titleSearch" class="form-control" type="text" name="q" class="q"
                                       placeholder="Title" value="" autofocus>

                            </div>

                        </div>

                        <div class="col-sm-6 col-lg-4">

                            <div class="form-group">

                                <label for="cveSearch" class="control-label text-primary">CVE</label>

                                <input id="cveSearch" class="form-control" type="text" name="cve" class="cve"
                                       placeholder="2024-1234"
                                       value="" autofocus>

                            </div>

                        </div>

                    </div>

                    <div class="row">

                        <div class="col-sm-6 col-lg-4">

                            <label for="typeSearchSelect" class="text-primary">Type</label>

                            <select id="typeSearchSelect" name="type" class="form-control">

                                <option></option>
                                
                                    <option value="dos" >
                                        dos
                                    </option>


                                
                                    <option value="local" >
                                        local
                                    </option>


                                
                                    <option value="remote" >
                                        remote
                                    </option>


                                
                                    <option value="shellcode" >
                                        shellcode
                                    </option>


                                
                                    <option value="papers" >
                                        papers
                                    </option>


                                
                                    <option value="webapps" >
                                        webapps
                                    </option>


                                
                            </select>

                        </div>

                        <div class="col-sm-6 col-lg-4">

                            <label for="platformSearchSelect" class="text-primary">Platform</label>

                            <select id="platformSearchSelect" name="platform" class="form-control">

                                <option></option>
                                
                                    <option value="aix" >
                                        AIX
                                    </option>

                                
                                    <option value="asp" >
                                        ASP
                                    </option>

                                
                                    <option value="bsd" >
                                        BSD
                                    </option>

                                
                                    <option value="bsd_ppc" >
                                        BSD_PPC
                                    </option>

                                
                                    <option value="bsd_x86" >
                                        BSD_x86
                                    </option>

                                
                                    <option value="bsdi_x86" >
                                        BSDi_x86
                                    </option>

                                
                                    <option value="cgi" >
                                        CGI
                                    </option>

                                
                                    <option value="freebsd" >
                                        FreeBSD
                                    </option>

                                
                                    <option value="freebsd_x86" >
                                        FreeBSD_x86
                                    </option>

                                
                                    <option value="freebsd_x86-64" >
                                        FreeBSD_x86-64
                                    </option>

                                
                                    <option value="generator" >
                                        Generator
                                    </option>

                                
                                    <option value="hardware" >
                                        Hardware
                                    </option>

                                
                                    <option value="hp-ux" >
                                        HP-UX
                                    </option>

                                
                                    <option value="irix" >
                                        IRIX
                                    </option>

                                
                                    <option value="jsp" >
                                        JSP
                                    </option>

                                
                                    <option value="linux" >
                                        Linux
                                    </option>

                                
                                    <option value="linux_mips" >
                                        Linux_MIPS
                                    </option>

                                
                                    <option value="linux_ppc" >
                                        Linux_PPC
                                    </option>

                                
                                    <option value="linux_sparc" >
                                        Linux_SPARC
                                    </option>

                                
                                    <option value="linux_x86" >
                                        Linux_x86
                                    </option>

                                
                                    <option value="linux_x86-64" >
                                        Linux_x86-64
                                    </option>

                                
                                    <option value="minix" >
                                        MINIX
                                    </option>

                                
                                    <option value="multiple" >
                                        Multiple
                                    </option>

                                
                                    <option value="netbsd_x86" >
                                        NetBSD_x86
                                    </option>

                                
                                    <option value="novell" >
                                        Novell
                                    </option>

                                
                                    <option value="openbsd" >
                                        OpenBSD
                                    </option>

                                
                                    <option value="openbsd_x86" >
                                        OpenBSD_x86
                                    </option>

                                
                                    <option value="osx_ppc" >
                                        OSX_PPC
                                    </option>

                                
                                    <option value="osx" >
                                        OSX
                                    </option>

                                
                                    <option value="php" >
                                        PHP
                                    </option>

                                
                                    <option value="plan9" >
                                        Plan9
                                    </option>

                                
                                    <option value="qnx" >
                                        QNX
                                    </option>

                                
                                    <option value="sco" >
                                        SCO
                                    </option>

                                
                                    <option value="sco_x86" >
                                        SCO_x86
                                    </option>

                                
                                    <option value="solaris" >
                                        Solaris
                                    </option>

                                
                                    <option value="solaris_sparc" >
                                        Solaris_SPARC
                                    </option>

                                
                                    <option value="solaris_x86" >
                                        Solaris_x86
                                    </option>

                                
                                    <option value="tru64" >
                                        Tru64
                                    </option>

                                
                                    <option value="ultrix" >
                                        ULTRIX
                                    </option>

                                
                                    <option value="unix" >
                                        Unix
                                    </option>

                                
                                    <option value="unixware" >
                                        UnixWare
                                    </option>

                                
                                    <option value="windows_x86" >
                                        Windows_x86
                                    </option>

                                
                                    <option value="windows_x86-64" >
                                        Windows_x86-64
                                    </option>

                                
                                    <option value="windows" >
                                        Windows
                                    </option>

                                
                                    <option value="arm" >
                                        ARM
                                    </option>

                                
                                    <option value="cfm" >
                                        CFM
                                    </option>

                                
                                    <option value="netware" >
                                        Netware
                                    </option>

                                
                                    <option value="superh_sh4" >
                                        SuperH_SH4
                                    </option>

                                
                                    <option value="java" >
                                        Java
                                    </option>

                                
                                    <option value="beos" >
                                        BeOS
                                    </option>

                                
                                    <option value="immunix" >
                                        Immunix
                                    </option>

                                
                                    <option value="palm_os" >
                                        Palm_OS
                                    </option>

                                
                                    <option value="atheos" >
                                        AtheOS
                                    </option>

                                
                                    <option value="ios" >
                                        iOS
                                    </option>

                                
                                    <option value="android" >
                                        Android
                                    </option>

                                
                                    <option value="xml" >
                                        XML
                                    </option>

                                
                                    <option value="perl" >
                                        Perl
                                    </option>

                                
                                    <option value="python" >
                                        Python
                                    </option>

                                
                                    <option value="system_z" >
                                        System_z
                                    </option>

                                
                                    <option value="json" >
                                        JSON
                                    </option>

                                
                                    <option value="ashx" >
                                        ASHX
                                    </option>

                                
                                    <option value="ruby" >
                                        Ruby
                                    </option>

                                
                                    <option value="aspx" >
                                        ASPX
                                    </option>

                                
                                    <option value="macos" >
                                        macOS
                                    </option>

                                
                                    <option value="linux_crisv32" >
                                        Linux_CRISv32
                                    </option>

                                
                                    <option value="ezine" >
                                        eZine
                                    </option>

                                
                                    <option value="magazine" >
                                        Magazine
                                    </option>

                                
                                    <option value="nodejs" >
                                        NodeJS
                                    </option>

                                
                                    <option value="alpha" >
                                        Alpha
                                    </option>

                                
                                    <option value="solaris_mips" >
                                        Solaris_MIPS
                                    </option>

                                
                                    <option value="lua" >
                                        Lua
                                    </option>

                                
                                    <option value="watchos" >
                                        watchOS
                                    </option>

                                
                                    <option value="vxworks" >
                                        VxWorks
                                    </option>

                                
                                    <option value="python2" >
                                        Python2
                                    </option>

                                
                                    <option value="python3" >
                                        Python3
                                    </option>

                                
                                    <option value="typescript" >
                                        TypeScript
                                    </option>

                                
                                    <option value="go" >
                                        Go
                                    </option>

                                
                            </select>

                        </div>

                        <div class="col-sm-6 col-lg-4">

                            <div class="form-group">

                                <label for="authorSearch" class="text-primary">Author</label>

                                <input id="authorSearch" class="form-control" type="text" name="e_author"
                                       placeholder="Author" value="">

                            </div>
                        </div>

                    </div>

                    <div class="row">

                        <div class="col-sm-12 col-lg-6">

                            <div class="form-group">

                                <label for="textSearch" class="control-label text-primary">Content</label>

                                <input id="textSearch" class="form-control" type="text" name="text"
                                       placeholder="Exploit content" value="">

                            </div>

                        </div>

                        <div class="col-sm-6 col-lg-2">

                            <label for="portSearchSelect" class="text-primary">Port</label>

                            <select id="portSearchSelect" name="port" class="form-control">

                                <option></option>
                                
                                    <option value="14" >
                                        14
                                    </option>


                                
                                    <option value="21" >
                                        21
                                    </option>


                                
                                    <option value="22" >
                                        22
                                    </option>


                                
                                    <option value="23" >
                                        23
                                    </option>


                                
                                    <option value="25" >
                                        25
                                    </option>


                                
                                    <option value="42" >
                                        42
                                    </option>


                                
                                    <option value="49" >
                                        49
                                    </option>


                                
                                    <option value="53" >
                                        53
                                    </option>


                                
                                    <option value="66" >
                                        66
                                    </option>


                                
                                    <option value="69" >
                                        69
                                    </option>


                                
                                    <option value="70" >
                                        70
                                    </option>


                                
                                    <option value="79" >
                                        79
                                    </option>


                                
                                    <option value="80" >
                                        80
                                    </option>


                                
                                    <option value="81" >
                                        81
                                    </option>


                                
                                    <option value="102" >
                                        102
                                    </option>


                                
                                    <option value="105" >
                                        105
                                    </option>


                                
                                    <option value="110" >
                                        110
                                    </option>


                                
                                    <option value="111" >
                                        111
                                    </option>


                                
                                    <option value="113" >
                                        113
                                    </option>


                                
                                    <option value="119" >
                                        119
                                    </option>


                                
                                    <option value="123" >
                                        123
                                    </option>


                                
                                    <option value="135" >
                                        135
                                    </option>


                                
                                    <option value="139" >
                                        139
                                    </option>


                                
                                    <option value="143" >
                                        143
                                    </option>


                                
                                    <option value="161" >
                                        161
                                    </option>


                                
                                    <option value="162" >
                                        162
                                    </option>


                                
                                    <option value="164" >
                                        164
                                    </option>


                                
                                    <option value="383" >
                                        383
                                    </option>


                                
                                    <option value="389" >
                                        389
                                    </option>


                                
                                    <option value="402" >
                                        402
                                    </option>


                                
                                    <option value="406" >
                                        406
                                    </option>


                                
                                    <option value="411" >
                                        411
                                    </option>


                                
                                    <option value="443" >
                                        443
                                    </option>


                                
                                    <option value="444" >
                                        444
                                    </option>


                                
                                    <option value="445" >
                                        445
                                    </option>


                                
                                    <option value="446" >
                                        446
                                    </option>


                                
                                    <option value="502" >
                                        502
                                    </option>


                                
                                    <option value="504" >
                                        504
                                    </option>


                                
                                    <option value="513" >
                                        513
                                    </option>


                                
                                    <option value="514" >
                                        514
                                    </option>


                                
                                    <option value="515" >
                                        515
                                    </option>


                                
                                    <option value="532" >
                                        532
                                    </option>


                                
                                    <option value="548" >
                                        548
                                    </option>


                                
                                    <option value="554" >
                                        554
                                    </option>


                                
                                    <option value="555" >
                                        555
                                    </option>


                                
                                    <option value="617" >
                                        617
                                    </option>


                                
                                    <option value="623" >
                                        623
                                    </option>


                                
                                    <option value="631" >
                                        631
                                    </option>


                                
                                    <option value="655" >
                                        655
                                    </option>


                                
                                    <option value="689" >
                                        689
                                    </option>


                                
                                    <option value="783" >
                                        783
                                    </option>


                                
                                    <option value="787" >
                                        787
                                    </option>


                                
                                    <option value="808" >
                                        808
                                    </option>


                                
                                    <option value="873" >
                                        873
                                    </option>


                                
                                    <option value="888" >
                                        888
                                    </option>


                                
                                    <option value="901" >
                                        901
                                    </option>


                                
                                    <option value="998" >
                                        998
                                    </option>


                                
                                    <option value="1000" >
                                        1000
                                    </option>


                                
                                    <option value="1040" >
                                        1040
                                    </option>


                                
                                    <option value="1089" >
                                        1089
                                    </option>


                                
                                    <option value="1099" >
                                        1099
                                    </option>


                                
                                    <option value="1100" >
                                        1100
                                    </option>


                                
                                    <option value="1114" >
                                        1114
                                    </option>


                                
                                    <option value="1120" >
                                        1120
                                    </option>


                                
                                    <option value="1194" >
                                        1194
                                    </option>


                                
                                    <option value="1235" >
                                        1235
                                    </option>


                                
                                    <option value="1471" >
                                        1471
                                    </option>


                                
                                    <option value="1521" >
                                        1521
                                    </option>


                                
                                    <option value="1533" >
                                        1533
                                    </option>


                                
                                    <option value="1581" >
                                        1581
                                    </option>


                                
                                    <option value="1589" >
                                        1589
                                    </option>


                                
                                    <option value="1604" >
                                        1604
                                    </option>


                                
                                    <option value="1617" >
                                        1617
                                    </option>


                                
                                    <option value="1723" >
                                        1723
                                    </option>


                                
                                    <option value="1743" >
                                        1743
                                    </option>


                                
                                    <option value="1761" >
                                        1761
                                    </option>


                                
                                    <option value="1812" >
                                        1812
                                    </option>


                                
                                    <option value="1858" >
                                        1858
                                    </option>


                                
                                    <option value="1861" >
                                        1861
                                    </option>


                                
                                    <option value="1900" >
                                        1900
                                    </option>


                                
                                    <option value="1947" >
                                        1947
                                    </option>


                                
                                    <option value="2000" >
                                        2000
                                    </option>


                                
                                    <option value="2022" >
                                        2022
                                    </option>


                                
                                    <option value="2049" >
                                        2049
                                    </option>


                                
                                    <option value="2100" >
                                        2100
                                    </option>


                                
                                    <option value="2103" >
                                        2103
                                    </option>


                                
                                    <option value="2121" >
                                        2121
                                    </option>


                                
                                    <option value="2125" >
                                        2125
                                    </option>


                                
                                    <option value="2181" >
                                        2181
                                    </option>


                                
                                    <option value="2242" >
                                        2242
                                    </option>


                                
                                    <option value="2315" >
                                        2315
                                    </option>


                                
                                    <option value="2375" >
                                        2375
                                    </option>


                                
                                    <option value="2380" >
                                        2380
                                    </option>


                                
                                    <option value="2381" >
                                        2381
                                    </option>


                                
                                    <option value="2401" >
                                        2401
                                    </option>


                                
                                    <option value="2480" >
                                        2480
                                    </option>


                                
                                    <option value="2525" >
                                        2525
                                    </option>


                                
                                    <option value="2640" >
                                        2640
                                    </option>


                                
                                    <option value="2810" >
                                        2810
                                    </option>


                                
                                    <option value="2812" >
                                        2812
                                    </option>


                                
                                    <option value="2947" >
                                        2947
                                    </option>


                                
                                    <option value="2954" >
                                        2954
                                    </option>


                                
                                    <option value="2990" >
                                        2990
                                    </option>


                                
                                    <option value="3000" >
                                        3000
                                    </option>


                                
                                    <option value="3030" >
                                        3030
                                    </option>


                                
                                    <option value="3050" >
                                        3050
                                    </option>


                                
                                    <option value="3052" >
                                        3052
                                    </option>


                                
                                    <option value="3128" >
                                        3128
                                    </option>


                                
                                    <option value="3129" >
                                        3129
                                    </option>


                                
                                    <option value="3181" >
                                        3181
                                    </option>


                                
                                    <option value="3200" >
                                        3200
                                    </option>


                                
                                    <option value="3217" >
                                        3217
                                    </option>


                                
                                    <option value="3306" >
                                        3306
                                    </option>


                                
                                    <option value="3333" >
                                        3333
                                    </option>


                                
                                    <option value="3378" >
                                        3378
                                    </option>


                                
                                    <option value="3389" >
                                        3389
                                    </option>


                                
                                    <option value="3460" >
                                        3460
                                    </option>


                                
                                    <option value="3465" >
                                        3465
                                    </option>


                                
                                    <option value="3500" >
                                        3500
                                    </option>


                                
                                    <option value="3535" >
                                        3535
                                    </option>


                                
                                    <option value="3632" >
                                        3632
                                    </option>


                                
                                    <option value="3690" >
                                        3690
                                    </option>


                                
                                    <option value="3790" >
                                        3790
                                    </option>


                                
                                    <option value="3814" >
                                        3814
                                    </option>


                                
                                    <option value="3817" >
                                        3817
                                    </option>


                                
                                    <option value="4000" >
                                        4000
                                    </option>


                                
                                    <option value="4002" >
                                        4002
                                    </option>


                                
                                    <option value="4070" >
                                        4070
                                    </option>


                                
                                    <option value="4081" >
                                        4081
                                    </option>


                                
                                    <option value="4105" >
                                        4105
                                    </option>


                                
                                    <option value="4111" >
                                        4111
                                    </option>


                                
                                    <option value="4322" >
                                        4322
                                    </option>


                                
                                    <option value="4343" >
                                        4343
                                    </option>


                                
                                    <option value="4434" >
                                        4434
                                    </option>


                                
                                    <option value="4444" >
                                        4444
                                    </option>


                                
                                    <option value="4501" >
                                        4501
                                    </option>


                                
                                    <option value="4555" >
                                        4555
                                    </option>


                                
                                    <option value="4592" >
                                        4592
                                    </option>


                                
                                    <option value="4661" >
                                        4661
                                    </option>


                                
                                    <option value="4750" >
                                        4750
                                    </option>


                                
                                    <option value="4848" >
                                        4848
                                    </option>


                                
                                    <option value="5000" >
                                        5000
                                    </option>


                                
                                    <option value="5060" >
                                        5060
                                    </option>


                                
                                    <option value="5061" >
                                        5061
                                    </option>


                                
                                    <option value="5080" >
                                        5080
                                    </option>


                                
                                    <option value="5081" >
                                        5081
                                    </option>


                                
                                    <option value="5093" >
                                        5093
                                    </option>


                                
                                    <option value="5151" >
                                        5151
                                    </option>


                                
                                    <option value="5180" >
                                        5180
                                    </option>


                                
                                    <option value="5247" >
                                        5247
                                    </option>


                                
                                    <option value="5250" >
                                        5250
                                    </option>


                                
                                    <option value="5272" >
                                        5272
                                    </option>


                                
                                    <option value="5308" >
                                        5308
                                    </option>


                                
                                    <option value="5432" >
                                        5432
                                    </option>


                                
                                    <option value="5466" >
                                        5466
                                    </option>


                                
                                    <option value="5554" >
                                        5554
                                    </option>


                                
                                    <option value="5555" >
                                        5555
                                    </option>


                                
                                    <option value="5600" >
                                        5600
                                    </option>


                                
                                    <option value="5655" >
                                        5655
                                    </option>


                                
                                    <option value="5666" >
                                        5666
                                    </option>


                                
                                    <option value="5800" >
                                        5800
                                    </option>


                                
                                    <option value="5803" >
                                        5803
                                    </option>


                                
                                    <option value="5814" >
                                        5814
                                    </option>


                                
                                    <option value="5858" >
                                        5858
                                    </option>


                                
                                    <option value="5900" >
                                        5900
                                    </option>


                                
                                    <option value="5984" >
                                        5984
                                    </option>


                                
                                    <option value="6066" >
                                        6066
                                    </option>


                                
                                    <option value="6070" >
                                        6070
                                    </option>


                                
                                    <option value="6080" >
                                        6080
                                    </option>


                                
                                    <option value="6082" >
                                        6082
                                    </option>


                                
                                    <option value="6101" >
                                        6101
                                    </option>


                                
                                    <option value="6112" >
                                        6112
                                    </option>


                                
                                    <option value="6129" >
                                        6129
                                    </option>


                                
                                    <option value="6379" >
                                        6379
                                    </option>


                                
                                    <option value="6502" >
                                        6502
                                    </option>


                                
                                    <option value="6503" >
                                        6503
                                    </option>


                                
                                    <option value="6660" >
                                        6660
                                    </option>


                                
                                    <option value="6667" >
                                        6667
                                    </option>


                                
                                    <option value="7001" >
                                        7001
                                    </option>


                                
                                    <option value="7002" >
                                        7002
                                    </option>


                                
                                    <option value="7070" >
                                        7070
                                    </option>


                                
                                    <option value="7071" >
                                        7071
                                    </option>


                                
                                    <option value="7080" >
                                        7080
                                    </option>


                                
                                    <option value="7100" >
                                        7100
                                    </option>


                                
                                    <option value="7144" >
                                        7144
                                    </option>


                                
                                    <option value="7210" >
                                        7210
                                    </option>


                                
                                    <option value="7272" >
                                        7272
                                    </option>


                                
                                    <option value="7290" >
                                        7290
                                    </option>


                                
                                    <option value="7426" >
                                        7426
                                    </option>


                                
                                    <option value="7443" >
                                        7443
                                    </option>


                                
                                    <option value="7510" >
                                        7510
                                    </option>


                                
                                    <option value="7547" >
                                        7547
                                    </option>


                                
                                    <option value="7649" >
                                        7649
                                    </option>


                                
                                    <option value="7770" >
                                        7770
                                    </option>


                                
                                    <option value="7777" >
                                        7777
                                    </option>


                                
                                    <option value="7778" >
                                        7778
                                    </option>


                                
                                    <option value="7787" >
                                        7787
                                    </option>


                                
                                    <option value="7879" >
                                        7879
                                    </option>


                                
                                    <option value="7902" >
                                        7902
                                    </option>


                                
                                    <option value="8000" >
                                        8000
                                    </option>


                                
                                    <option value="8001" >
                                        8001
                                    </option>


                                
                                    <option value="8002" >
                                        8002
                                    </option>


                                
                                    <option value="8004" >
                                        8004
                                    </option>


                                
                                    <option value="8008" >
                                        8008
                                    </option>


                                
                                    <option value="8020" >
                                        8020
                                    </option>


                                
                                    <option value="8022" >
                                        8022
                                    </option>


                                
                                    <option value="8023" >
                                        8023
                                    </option>


                                
                                    <option value="8028" >
                                        8028
                                    </option>


                                
                                    <option value="8030" >
                                        8030
                                    </option>


                                
                                    <option value="8080" >
                                        8080
                                    </option>


                                
                                    <option value="8081" >
                                        8081
                                    </option>


                                
                                    <option value="8082" >
                                        8082
                                    </option>


                                
                                    <option value="8088" >
                                        8088
                                    </option>


                                
                                    <option value="8090" >
                                        8090
                                    </option>


                                
                                    <option value="8181" >
                                        8181
                                    </option>


                                
                                    <option value="8300" >
                                        8300
                                    </option>


                                
                                    <option value="8400" >
                                        8400
                                    </option>


                                
                                    <option value="8443" >
                                        8443
                                    </option>


                                
                                    <option value="8445" >
                                        8445
                                    </option>


                                
                                    <option value="8473" >
                                        8473
                                    </option>


                                
                                    <option value="8500" >
                                        8500
                                    </option>


                                
                                    <option value="8585" >
                                        8585
                                    </option>


                                
                                    <option value="8619" >
                                        8619
                                    </option>


                                
                                    <option value="8800" >
                                        8800
                                    </option>


                                
                                    <option value="8812" >
                                        8812
                                    </option>


                                
                                    <option value="8839" >
                                        8839
                                    </option>


                                
                                    <option value="8880" >
                                        8880
                                    </option>


                                
                                    <option value="8888" >
                                        8888
                                    </option>


                                
                                    <option value="9000" >
                                        9000
                                    </option>


                                
                                    <option value="9001" >
                                        9001
                                    </option>


                                
                                    <option value="9002" >
                                        9002
                                    </option>


                                
                                    <option value="9080" >
                                        9080
                                    </option>


                                
                                    <option value="9090" >
                                        9090
                                    </option>


                                
                                    <option value="9091" >
                                        9091
                                    </option>


                                
                                    <option value="9100" >
                                        9100
                                    </option>


                                
                                    <option value="9124" >
                                        9124
                                    </option>


                                
                                    <option value="9200" >
                                        9200
                                    </option>


                                
                                    <option value="9251" >
                                        9251
                                    </option>


                                
                                    <option value="9256" >
                                        9256
                                    </option>


                                
                                    <option value="9443" >
                                        9443
                                    </option>


                                
                                    <option value="9447" >
                                        9447
                                    </option>


                                
                                    <option value="9784" >
                                        9784
                                    </option>


                                
                                    <option value="9788" >
                                        9788
                                    </option>


                                
                                    <option value="9855" >
                                        9855
                                    </option>


                                
                                    <option value="9876" >
                                        9876
                                    </option>


                                
                                    <option value="9900" >
                                        9900
                                    </option>


                                
                                    <option value="9987" >
                                        9987
                                    </option>


                                
                                    <option value="9993" >
                                        9993
                                    </option>


                                
                                    <option value="9999" >
                                        9999
                                    </option>


                                
                                    <option value="10000" >
                                        10000
                                    </option>


                                
                                    <option value="10001" >
                                        10001
                                    </option>


                                
                                    <option value="10080" >
                                        10080
                                    </option>


                                
                                    <option value="10202" >
                                        10202
                                    </option>


                                
                                    <option value="10203" >
                                        10203
                                    </option>


                                
                                    <option value="10443" >
                                        10443
                                    </option>


                                
                                    <option value="10616" >
                                        10616
                                    </option>


                                
                                    <option value="11000" >
                                        11000
                                    </option>


                                
                                    <option value="11211" >
                                        11211
                                    </option>


                                
                                    <option value="11460" >
                                        11460
                                    </option>


                                
                                    <option value="12203" >
                                        12203
                                    </option>


                                
                                    <option value="12221" >
                                        12221
                                    </option>


                                
                                    <option value="12345" >
                                        12345
                                    </option>


                                
                                    <option value="12397" >
                                        12397
                                    </option>


                                
                                    <option value="12401" >
                                        12401
                                    </option>


                                
                                    <option value="13327" >
                                        13327
                                    </option>


                                
                                    <option value="13701" >
                                        13701
                                    </option>


                                
                                    <option value="13722" >
                                        13722
                                    </option>


                                
                                    <option value="13838" >
                                        13838
                                    </option>


                                
                                    <option value="16992" >
                                        16992
                                    </option>


                                
                                    <option value="18821" >
                                        18821
                                    </option>


                                
                                    <option value="18881" >
                                        18881
                                    </option>


                                
                                    <option value="19000" >
                                        19000
                                    </option>


                                
                                    <option value="19810" >
                                        19810
                                    </option>


                                
                                    <option value="19813" >
                                        19813
                                    </option>


                                
                                    <option value="20000" >
                                        20000
                                    </option>


                                
                                    <option value="20002" >
                                        20002
                                    </option>


                                
                                    <option value="20010" >
                                        20010
                                    </option>


                                
                                    <option value="20031" >
                                        20031
                                    </option>


                                
                                    <option value="20111" >
                                        20111
                                    </option>


                                
                                    <option value="20171" >
                                        20171
                                    </option>


                                
                                    <option value="22003" >
                                        22003
                                    </option>


                                
                                    <option value="23423" >
                                        23423
                                    </option>


                                
                                    <option value="25672" >
                                        25672
                                    </option>


                                
                                    <option value="26000" >
                                        26000
                                    </option>


                                
                                    <option value="27015" >
                                        27015
                                    </option>


                                
                                    <option value="27700" >
                                        27700
                                    </option>


                                
                                    <option value="28015" >
                                        28015
                                    </option>


                                
                                    <option value="30000" >
                                        30000
                                    </option>


                                
                                    <option value="30303" >
                                        30303
                                    </option>


                                
                                    <option value="31337" >
                                        31337
                                    </option>


                                
                                    <option value="32400" >
                                        32400
                                    </option>


                                
                                    <option value="32674" >
                                        32674
                                    </option>


                                
                                    <option value="32764" >
                                        32764
                                    </option>


                                
                                    <option value="34205" >
                                        34205
                                    </option>


                                
                                    <option value="37215" >
                                        37215
                                    </option>


                                
                                    <option value="37777" >
                                        37777
                                    </option>


                                
                                    <option value="37848" >
                                        37848
                                    </option>


                                
                                    <option value="38292" >
                                        38292
                                    </option>


                                
                                    <option value="40007" >
                                        40007
                                    </option>


                                
                                    <option value="41523" >
                                        41523
                                    </option>


                                
                                    <option value="44334" >
                                        44334
                                    </option>


                                
                                    <option value="46824" >
                                        46824
                                    </option>


                                
                                    <option value="48080" >
                                        48080
                                    </option>


                                
                                    <option value="49152" >
                                        49152
                                    </option>


                                
                                    <option value="50000" >
                                        50000
                                    </option>


                                
                                    <option value="50496" >
                                        50496
                                    </option>


                                
                                    <option value="52311" >
                                        52311
                                    </option>


                                
                                    <option value="52789" >
                                        52789
                                    </option>


                                
                                    <option value="52869" >
                                        52869
                                    </option>


                                
                                    <option value="52986" >
                                        52986
                                    </option>


                                
                                    <option value="53413" >
                                        53413
                                    </option>


                                
                                    <option value="54345" >
                                        54345
                                    </option>


                                
                                    <option value="54890" >
                                        54890
                                    </option>


                                
                                    <option value="55554" >
                                        55554
                                    </option>


                                
                                    <option value="55555" >
                                        55555
                                    </option>


                                
                                    <option value="56380" >
                                        56380
                                    </option>


                                
                                    <option value="57772" >
                                        57772
                                    </option>


                                
                                    <option value="58080" >
                                        58080
                                    </option>


                                
                                    <option value="62514" >
                                        62514
                                    </option>


                                
                            </select>

                        </div>

                        <div class="col-sm-6 col-lg-4">

                            <label for="tagSearchSelect" class="text-primary">Tag</label>

                            <select id="tagSearchSelect" name="tag" class="form-control">

                                <option></option>
                                
                                    <option value="1" >
                                        WordPress Core
                                    </option>


                                
                                    <option value="3" >
                                        Metasploit Framework (MSF)
                                    </option>


                                
                                    <option value="4" >
                                        WordPress Plugin
                                    </option>


                                
                                    <option value="7" >
                                        SQL Injection (SQLi)
                                    </option>


                                
                                    <option value="8" >
                                        Cross-Site Scripting (XSS)
                                    </option>


                                
                                    <option value="9" >
                                        File Inclusion (LFI/RFI)
                                    </option>


                                
                                    <option value="12" >
                                        Cross-Site Request Forgery (CSRF)
                                    </option>


                                
                                    <option value="13" >
                                        Denial of Service (DoS)
                                    </option>


                                
                                    <option value="14" >
                                        Code Injection
                                    </option>


                                
                                    <option value="15" >
                                        Command Injection
                                    </option>


                                
                                    <option value="16" >
                                        Authentication Bypass / Credentials Bypass (AB/CB)
                                    </option>


                                
                                    <option value="18" >
                                        Client Side
                                    </option>


                                
                                    <option value="19" >
                                        Use After Free (UAF)
                                    </option>


                                
                                    <option value="20" >
                                        Out Of Bounds
                                    </option>


                                
                                    <option value="21" >
                                        Remote
                                    </option>


                                
                                    <option value="22" >
                                        Local
                                    </option>


                                
                                    <option value="23" >
                                        XML External Entity (XXE)
                                    </option>


                                
                                    <option value="24" >
                                        Integer Overflow
                                    </option>


                                
                                    <option value="25" >
                                        Server-Side Request Forgery (SSRF)
                                    </option>


                                
                                    <option value="26" >
                                        Race Condition
                                    </option>


                                
                                    <option value="27" >
                                        NULL Pointer Dereference
                                    </option>


                                
                                    <option value="28" >
                                        Malware
                                    </option>


                                
                                    <option value="31" >
                                        Buffer Overflow
                                    </option>


                                
                                    <option value="34" >
                                        Heap Overflow
                                    </option>


                                
                                    <option value="35" >
                                        Type Confusion
                                    </option>


                                
                                    <option value="36" >
                                        Object Injection
                                    </option>


                                
                                    <option value="37" >
                                        Bug Report
                                    </option>


                                
                                    <option value="38" >
                                        Console
                                    </option>


                                
                                    <option value="39" >
                                        Pwn2Own
                                    </option>


                                
                                    <option value="40" >
                                        Traversal
                                    </option>


                                
                                    <option value="41" >
                                        Deserialization
                                    </option>


                                
                            </select>

                        </div>

                    </div>

                    <div class="row">

                        <div class="col-12">

                            <div class="form-check form-check-inline">

                                <label class="form-check-label text-primary">

                                    <input class="form-check-input" type="checkbox"
                                           name="verified" value="true"
                                           id="verifiedSearchCheck"   >
                                    Verified

                                    <span class="form-check-sign">
                                        <span class="check"></span>
                                    </span>

                                </label>

                            </div>

                            <div class="form-check form-check-inline">

                                <label class="form-check-label text-primary">
                                    <input class="form-check-input" type="checkbox"
                                           name="hasapp" value="true"
                                           id="hasappSearchCheck" >
                                    Has App

                                    <span class="form-check-sign">
                                        <span class="check"></span>
                                    </span>

                                </label>

                            </div>

                            <div class="form-check form-check-inline">

                                <label class="form-check-label text-primary">
                                    <input class="form-check-input" type="checkbox"
                                           name="nomsf" value="true"
                                           id="nomsfCheck" >
                                    No Metasploit

                                    <span class="form-check-sign">
                                        <span class="check"></span>
                                    </span>

                                </label>

                            </div>

                        </div>

                    </div>

                    <div class="row">

                        <div class="col-12">

                            <button type="submit" class="btn btn-primary float-right">Search</button>

                        </div>

                    </div>

                </form>


            </div>

        </div>

    </div>

</div>

</footer>

    </div>

</div>

</body>

<!--   Make the default DataTables search field larger   -->
<style type="text/css">
    .dataTables_filter input {
        font-size: 16px;
    }
</style>

<!--   Core JS Files   -->
<script src="/js/core/jquery.min.js"></script>
<script src="/js/core/popper.min.js"></script>
<script src="/js/core/bootstrap.min.js"></script>

<script src="/js/plugins/perfect-scrollbar.jquery.min.js"></script>
<script src="/js/plugins/moment.min.js"></script>

<!-- Forms Validations Plugin -->
<script src="/js/plugins/jquery.validate.min.js"></script>

<!--  DataTables.net Plugin, full documentation here:
https://datatables.net/    -->
<script src="/js/plugins/jquery.dataTables.min.js"></script>

<!--  Notifications Plugin    -->
<script src="/js/plugins/bootstrap-notify.js"></script>

<!-- Control Center for Now Ui Dashboard: parallax effects,
scripts for the example pages etc -->
<script src="/js/now-ui-dashboard.js"></script>

<script src="/js/selectize.min.js"></script>

<script src="/js/app.js"></script>
<script src="/js/appfunctions.js"></script>


<script>
    window.addEventListener('popstate', () => {
        location.reload();
    }, false);

    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    })

    function getParameterByName(name, url) {
        if (!url) url = window.location.href;
        name = name.replace(/[\[\]]/g, "\\$&");
        var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
            results = regex.exec(url);
        if (!results) return null;
        if (!results[2]) return '';
        return decodeURIComponent(results[2].replace(/\+/g, " "));
    }


    function removeURLParameter(url, parameter) {
        //prefer to use l.search if you have a location/link object
        var urlparts= url.split('?');
        if (urlparts.length>=2) {

            var prefix= encodeURIComponent(parameter)+'=';
            var pars= urlparts[1].split(/[&;]/g);

            //reverse iteration as may be destructive
            for (var i= pars.length; i-- > 0;) {
                //idiom for string.startsWith
                if (pars[i].lastIndexOf(prefix, 0) !== -1) {
                    pars.splice(i, 1);
                }
            }

            url= urlparts[0] + (pars.length > 0 ? '?' + pars.join('&') : "");
            window.history.pushState('', document.title, url);
            return url;
        } else {
            window.history.pushState('', document.title, url);
            return url;
        }
    }

    function showFilters() {
        var x = document.getElementById("exploitFiltersCard");
        if (x.style.display === "none") {
            x.style.display = "block";
        } else {
            x.style.display = "none";
        }
    }

    function updateQueryString(key, value, url) {
        if (!url) url = window.location.href;
        var re = new RegExp("([?&])" + key + "=.*?(&|#|$)(.*)", "gi"),
            hash;

        if (re.test(url)) {
            if (typeof value !== 'undefined' && value !== null)
                return url.replace(re, '$1' + key + "=" + value + '$2$3');
            else {
                hash = url.split('#');
                url = hash[0].replace(re, '$1$3').replace(/(&|\?)$/, '');
                if (typeof hash[1] !== 'undefined' && hash[1] !== null)
                    url += '#' + hash[1];

                window.history.pushState('', document.title, url);
                return url;
            }
        }
        else {
            if (typeof value !== 'undefined' && value !== null) {
                var separator = url.indexOf('?') !== -1 ? '&' : '?';
                hash = url.split('#');
                url = hash[0] + separator + key + '=' + value;
                if (typeof hash[1] !== 'undefined' && hash[1] !== null)
                    url += '#' + hash[1];

                window.history.pushState('', document.title, url);
                return url;
            }
            else
                window.history.pushState('', document.title, url);
                return url;
        }
    }

    $('#search').submit(function() {
        $(this).find(":input").filter(function(){ return !this.value; }).attr("disabled", "disabled");
        return true; // ensure form still submits
    });

    // Un-disable form fields when page loads, in case they click back after submission
    $('#search').find( ":input" ).prop( "disabled", false );

    // If the ajax call fails, throw the error to the console instead of
    // popping up an alert to the user
    $.fn.dataTable.ext.errMode = 'throw';

</script>

<!-- App scripts -->



</html>
