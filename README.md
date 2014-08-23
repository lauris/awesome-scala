Awesome Scala
=============

A community driven list of useful Scala libraries, frameworks and software. This is not a catalog of all the libraries, just a starting point for your explorations. Inspired by [awesome-python](https://github.com/vinta/awesome-python). Other amazingly awesome lists can be found in the [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) list.

- [Awesome Scala](#awesome-scala)
    - [Database](#database)
    - [Web Frameworks](#web-frameworks)
    - [i18n](#i18n)
    - [Authentication](#authentication)
    - [Testing](#testing)
    - [JSON Manipulation](#json-manipulation)
    - [Serialization](#serialization)
    - [Science and Data Analysis](#science-and-data-analysis)
    - [Big Data](#big-data)
    - [Functional Reactive Programming](#functional-reactive-programming)
    - [Modularization and Dependency Injection](#modularization-and-dependency-injection)
    - [Distributed Systems](#distributed-systems)
    - [Extensions](#extensions)
    - [Android](#android)
    - [HTTP](#http)
    - [Semantic Web](#semantic-web)
    - [Metrics and Monitoring](#metrics-and-monitoring)
    - [Sbt plugins](#sbt-plugins)
- [Contributing](#contributing)

## Database

*Database access libraries in Scala.*

* [ScalikeJDBC](https://github.com/scalikejdbc/scalikejdbc) — A tidy SQL-based DB access library for Scala developers.
* [Slick](https://github.com/slick/slick) — Modern database query and access library for Scala.
* [Squeryl](https://github.com/squeryl/squeryl) — A Scala DSL for talking with databases with minimum verbosity and maximum type safety.
* [Activate](https://github.com/fwbrasil/activate) — Pluggable object persistence in Scala.
* [Scala ActiveRecord](https://github.com/aselab/scala-activerecord) — ORM library for scala, inspired by ActiveRecord of Ruby on Rails.
* [PostgreSQL and MySQL async](https://github.com/mauricio/postgresql-async) — Async database drivers to talk to PostgreSQL and MySQL in Scala.
* [ReactiveMongo](https://github.com/ReactiveMongo/ReactiveMongo) — Reactive Scala Driver for MongoDB.
* [Phantom](https://github.com/websudosuk/phantom) — Async type safe Scala DSL for Apache Cassandra.
* [ReactiveCouchbase](http://reactivecouchbase.org/) — Reactive Scala Driver for Couchbase. Also includes a Play plug-in. An official plug-in is also in development.
* [Salat](https://github.com/novus/salat/) — ORM for MongoDB. A related Play-plugin is also available.
* [elastic4s](https://github.com/sksamuel/elastic4s) — Concise, idiomatic, asynchronous, type safe Scala Client for Elasticsearch.


## Web Frameworks

*Scala frameworks for web development.*

* [Play](https://github.com/playframework/playframework) — Makes it easy to build scalable, fast and real-time web applications with Java & Scala.
* [Lift](https://github.com/lift/framework) — Secure and powerful full stack web framework ([discussion](https://github.com/lauris/awesome-scala/pull/19)).
* [Skinny Framework](https://github.com/skinny-framework/skinny-framework) — A full-stack web app framework upon Scalatra for rapid Development in Scala.
* [Scalatra](https://github.com/scalatra/scalatra) — Tiny Scala high-performance, async web framework, inspired by Sinatra.
* [Spray](https://github.com/spray/spray) — A suite of scala libraries for building and consuming RESTful web services on top of Akka.
* [Finatra](https://github.com/twitter/finatra) — A sinatra-inspired web framework for scala, running on top of Finagle.
* [Reactive](https://github.com/nafg/reactive) — FRP and web abstractions, which can be plugged into any web framework (currently only has bindings for Lift).
* [Chaos](https://github.com/mesosphere/chaos) — A lightweight framework for writing REST services in Scala.
* [Xitrum](http://xitrum-framework.github.io/) — An async and clustered Scala web framework and HTTP(S) server fusion on top of Netty, Akka, and Hazelcast.
* [Unfiltered](https://github.com/unfiltered/unfiltered) — A modular set of unopinionated primitives for servicing HTTP and WebSocket requests in Scala.


## i18n

*Scala libraries for i18n.*

* [Scaposer](https://github.com/xitrum-framework/scaposer) – GNU Gettext .po file loader for Scala.
* [scala-xgettext](https://github.com/xitrum-framework/scala-xgettext) – A compiler plugin that acts like GNU xgettext command to extract i18n strings in Scala source code files to Gettext .po file.

## Authentication

*Libraries for implementing authentications schemes.*

* [scala-oauth2-provider](https://github.com/nulab/scala-oauth2-provider) — OAuth 2.0 server-side implementation written in Scala.
* [SecureSocial](https://github.com/jaliss/securesocial) — A module that provides OAuth, OAuth2 and OpenID authentication for Play Framework applications.
* [play2-auth](https://github.com/t2v/play2-auth) — Play2.x Authentication and Authorization module.
* [play-pac4j](https://github.com/leleuj/play-pac4j) — Profile & Authentication Client in Scala for CAS, OAuth, OpenID, SAML & HTTP protocols and Play 2.x framework.

## Testing

*Libraries for code testing.*

* [ScalaCheck](https://github.com/rickynils/scalacheck) — Property-based testing for Scala.
* [ScalaTest](https://github.com/scalatest/scalatest) — A testing tool for Scala and Java developers.
* [ScalaMeter](https://scalameter.github.io/) - Performance &  memory footprint measuring, regression testing.
* [Specs2](https://github.com/etorreborre/specs2) — Software Specifications for Scala.
* [µTest](https://github.com/lihaoyi/utest) — A tiny, portable testing library for Scala.
* [Scalive](https://github.com/xitrum-framework/scalive) — Connect a Scala REPL to running JVM processes without any prior setup; this library is used for inspecting systems in production mode.
* [Scalastyle](https://github.com/scalastyle/scalastyle) – Scala style checker.
* [Gatling](http://gatling-tool.org/) – Async Scala-Akka-Netty based Stress Tool.

## JSON Manipulation

*Libraries for work with json.*

* [json4s](https://github.com/json4s/json4s) — Project aims to provide a single AST to be used by other scala json libraries.
* [spray-json](https://github.com/spray/spray-json) — Lightweight, clean and efficient JSON implementation in Scala.
* [argonaut](http://argonaut.io/) — Purely Functional JSON in Scala.
* [jackson-module-scala](https://github.com/FasterXML/jackson-module-scala) — Add-on module for Jackson to support Scala-specific datatypes.
* [play-json](https://github.com/playframework/playframework/tree/master/framework/src/play-json) — Flexible and powerful JSON manipulation, validation and serialization, with no reflection at runtime.

## Serialization

*Libraries for serializing and deserializing data for storage or transport.*

* [Pickling](https://github.com/scala/pickling) — Fast, customizable, boilerplate-free pickling support.
* [scodec](https://github.com/scodec/scodec) — A combinator library for working with binary data.
* [Scrooge](http://twitter.github.io/scrooge/) — An Apache Thrift code generator for Scala.
* [validation](https://github.com/jto/validation) — Advanced validation & serialization for JSON, HTML form data, etc, with no reflection at runtime.

## Science and Data Analysis

*Libraries for scientific computing, data analysis and numerical processing.*

* [Algebird](https://github.com/twitter/algebird) — Abstract Algebra for Scala.
* [Breeze](https://github.com/scalanlp/breeze) — Breeze is a numerical processing library for Scala.
* [FACTORIE](https://github.com/factorie/factorie) — A toolkit for deployable probabilistic modeling, implemented as a software library in Scala.
* [Figaro](https://github.com/p2t2/figaro) - Figaro is a probabilistic programming language that supports development of very rich probabilistic models.
* [MGO](https://github.com/romainreuillon/mgo) — Modular multi-objective evolutionary algorithm optimization library enforcing immutability.
* [MLLib](https://spark.apache.org/mllib/) — Machine Learning framework for Spark
* [Saddle](https://github.com/saddle/saddle) — A minimalist port of Pandas to Scala
* [Spire](https://github.com/non/spire) — Powerful new number types and numeric abstractions for Scala.
* [Squants](https://github.com/garyKeorkunian/squants) — The Scala API for Quantities, Units of Measure and Dimensional Analysis.


## Big Data
* [Spark](http://spark.apache.org/) — Lightning fast cluster computing — up to 100x faster than Hadoop for iterative algorithms (memory caching) and up to 10x faster than Hadoop for single-pass MapReduce jobs. Compatible with YARN-enabled Hadoop clusters, can run on Mesos and in stand-alone mode as well.
* [Scalding](https://github.com/twitter/scalding) — A Scala binding for the Cascading abstraction of Hadoop MapReduce.
* [Summingbird](https://github.com/twitter/summingbird) — An implementation of the “lambda architecture” as a software abstraction — a single API for Hadoop and Storm.
* [Scrunch](http://crunch.apache.org/scrunch.html) — A Scala wrapper for [Apache Crunch](http://crunch.apache.org/index.html) which provides a framework for writing, testing, and running MapReduce pipelines.
* [GridScale](https://github.com/romainreuillon/gridscale) — A Scala API for computing clusters and grids.
* [scoozie](https://github.com/klout/scoozie) — Scala DSL on top of Oozie XML.

## Functional Reactive Programming

*Event streams, signals, observables, etc.*

* [Scala.Rx](https://github.com/lihaoyi/scala.rx) — An experimental library for Functional Reactive Programming in Scala (reactive variables). Scala.js compatible.
* [scala.frp](https://github.com/dylemma/scala.frp) — Functional Reactive Programming for Scala (event streams).
* [RxJava-Scala](https://github.com/Netflix/RxJava/tree/master/language-adaptors/rxjava-scala) — Scala Adaptor for RxJava.
* [Reactive Collections](https://github.com/storm-enroute/reactive-collections) – A library that incorporates event streams and signals with specialized collections called reactive containers, and expresses concurrency using isolates and channels.
* [Vertx.io](http://vertx.io/) – A polyglot reactive application platform for the JVM which aims to be an alternative to node.js. Its concurrency model resembles actors. It supports [Scala](http://vertx.io/core_manual_scala.html), Clojure, Java, Javascript, Ruby, Groovy and Python.

## Modularization and Dependency Injection

*Modularization of applications, dependency injection, etc.*

* [Domino](https://github.com/helgoboss/domino) — Write elegant OSGi bundle activators in Scala.
* [Sclasner](https://github.com/xitrum-framework/sclasner) - Scala classpath scanner.
* [Scaldi](https://github.com/scaldi/scaldi) — Lightweight Scala Dependency Injection Library.
* [MacWire](https://github.com/adamw/macwire) — Scala Macro to generate wiring code for class instantiation. DI container replacement.
* [SubCut](https://github.com/dickwall/subcut) — Scala Uniquely Bound Classes Under Traits.

## Distributed Systems

*Libraries and frameworks for writing distributed applications.*

* [Akka](http://akka.io/) — A toolkit and runtime for building highly concurrent, distributed, and fault tolerant event-driven applications.
* [Finagle](https://twitter.github.io/finagle/) — An extensible, protocol-agnostic RPC system designed for high performance and concurrency.
* [Glokka](https://github.com/xitrum-framework/glokka) - Library to register and lookup actors by names in an Akka cluster.

## Extensions

*Scala extensions.*

* [Scalaz](https://github.com/scalaz/scalaz) — An extension to the core Scala library for functional programming.
* [Shapeless](https://github.com/milessabin/shapeless) — A type class and dependent type based generic programming library for Scala.
* [Twitter Util](https://github.com/twitter/util) — General-purpose Scala libraries, including a future implementation and other concurrency tools.
* [Scala Async](https://github.com/scala/async) — An asynchronous programming facility for Scala.
* [Resolvable](https://github.com/resolvable/resolvable) — A library to optimize fetching immutable data structures from several endpoints in several formats.
* [Scala Blitz](http://scala-blitz.github.io/) – A library to speed up Scala collection operations by removing runtime overheads during compilation, and a custom data-parallel operation runtime.
* [Log4s](http://log4s.org) - Fast, Scala-friendly logging bindings on top of [SLF4J](http://slf4j.org/). Uses macros for extreme performance.
* [Lamma](https://github.com/maxcellent/lamma) – A Scala date library for date and schedule generation.
* [Scala Graph](http://www.scala-graph.org/) – A Scala library with basic graph functionality that seamlessly fits into the Scala standard collections library
* [Cassovary](https://github.com/twitter/cassovary) – A Scala library that is designed from the ground up for space efficiency, handling graphs with billions of nodes and edges.

## Android

*Scala libraries and wrappers for Android development.*

* [Scaloid](https://github.com/pocorall/scaloid) — Less painful Android development with Scala.
* [Macroid](https://github.com/macroid/macroid) — A modular functional UI language for Android.
* [Android SDK Plugin for SBT](https://github.com/pfn/android-sdk-plugin) — An sbt plugin that adds tasks for developing Android applications.

## HTTP

*Scala libraries and wrappers for HTTP clients.*

* [Dispatch](https://github.com/dispatch/reboot) — Library for asynchronous HTTP interaction. It provides a Scala vocabulary for Java’s [async-http-client](https://github.com/AsyncHttpClient/async-http-client).
* [Netcaty](https://github.com/ngocdaothanh/netcaty) - Simple net test client/server for Netty and Scala lovers.
* [Scalaxb](https://github.com/eed3si9n/scalaxb) — An XML data-binding tool for Scala that supports W3C XML Schema (xsd) and Web Services Description Language (wsdl) as the input file.
* [Spray](http://spray.io/) — Actor-based library for http interaction.
* [Tubesocks](https://github.com/softprops/tubesocks) — Library supporting bi-directional communication with websocket servers.
* [scalaj-http](https://github.com/scalaj/scalaj-http) – Simple scala wrapper for HttpURLConnection (including OAuth support).
* [Finch.io](https://github.com/finagle/finch) — Purely Functional REST API atop of [Finagle](https://github.com/twitter/finagle).
* [Newman](https://github.com/stackmob/newman) — A REST DSL that tries to take the best from Dispatch, Finagle and Apache HttpClient. See [here](https://www.paypal-engineering.com/2014/02/13/hello-newman-a-rest-client-for-scala/) for rationale.


## Semantic Web

*Scala libraries for interactions with the Web of Data, and other RDF tools*

* [Banana-RDF](https://github.com/w3c/banana-rdf) – Scala-friendly abstractions for RDF and Linked Data technologies. Supports Jena, Sesame and native Scala.

## Metrics and Monitoring

*Scala libraries for gathering metrics and monitoring applications.*

* [Kamon](http://kamon.io) - Gathering metrics from applications built with Akka, Spray and Play! with support for user metrics as well.


## Sbt plugins

*Sbt plugins to make your life easier*

* [Sbt-Revolver](https://github.com/spray/sbt-revolver) – Fork & Stop processes from sbt.
* [Sbt-Eclipse](https://github.com/typesafehub/sbteclipse) – Create Eclipse project definitions from sbt builds.
* [Sbt-Native-Packager](https://github.com/sbt/sbt-native-packager) – Bundle up Scala software for native packaging systems, like deb, rpm, homebrew, msi..
* [Sbt-Dependency-Graph](https://github.com/jrudolph/sbt-dependency-graph) – Create a dependency graph for your project.
* [Sbt-One-Jar](https://github.com/sbt/sbt-onejar) – Packages your project using One-JAR™.
* [Sbt-Start-Script](https://github.com/sbt/sbt-start-script) – Create a "start" script to run the program.
* [ScalaKata](https://github.com/MasseGuillaume/ScalaKata) – Scala playground & Documentation tool.
* [WartRemover](https://github.com/typelevel/wartremover) – Flexible Scala code linting tool.

# Contributing

Your contributions are always welcome! Please submit a pull request or create an issue to add a new framework, library or software to the list. Do not submit a project that hasn’t been updated in the past 6 months or is not awesome.
