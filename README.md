Awesome Scala [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
=============

A community driven list of useful Scala libraries, frameworks and software. This is not a catalog of all the libraries, just a starting point for your explorations. Inspired by [awesome-python](https://github.com/vinta/awesome-python). Other amazingly awesome lists can be found in the [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) list.

Projects with over 500 stargazers are in bold.

- [Awesome Scala](#awesome-scala)
    - [Database](#database)
    - [Graphical User Interfaces](#graphical-user-interfaces)
    - [Web Frameworks](#web-frameworks)
    - [i18n](#i18n)
    - [Authentication](#authentication)
    - [Authorization](#authorization)
    - [Testing](#testing)
    - [JSON Manipulation](#json-manipulation)
    - [Serialization](#serialization)
    - [Science and Data Analysis](#science-and-data-analysis)
    - [Big Data](#big-data)
    - [Image processing and image analysis](#image-processing-and-image-analysis)
    - [Functional Reactive Programming](#functional-reactive-programming)
    - [Modularization and Dependency Injection](#modularization-and-dependency-injection)
    - [Distributed Systems](#distributed-systems)
    - [Extensions](#extensions)
    - [Misc](#misc)
    - [Android](#android)
    - [HTTP](#http)
    - [Semantic Web](#semantic-web)
    - [Metrics and Monitoring](#metrics-and-monitoring)
    - [Parsing](#parsing)
    - [Sbt plugins](#sbt-plugins)
    - [XML / Html](#xml--html)
    - [Other](#other)
    - [Tools](#tools)
    - [Learning Scala](#learning-scala)
    - [JavaScript](#javascript)
- [Contributing](#contributing)

## Database

*Database access libraries in Scala.*

* [Activate ★ 272 ⧗ 0](https://github.com/fwbrasil/activate) - Pluggable object persistence in Scala.
* [Casbah](http://mongodb.github.io/casbah/) ([repo](https://github.com/mongodb/casbah)) - Officially supported Scala driver for MongoDB
* [doobie ★ 305 ⧗ 3](https://github.com/tpolecat/doobie) - Pure functional JDBC layer for Scala.
* [Elastic4s ★ 459 ⧗ 0](https://github.com/sksamuel/elastic4s) - A scala DSL / reactive client for Elasticsearch
* [MapperDao ★ 7 ⧗ 55](https://github.com/kostaskougios/mapperdao) - An ORM library for oracle, mysql, mssql, and postgresql
* [Memcontinuationed ★ 45 ⧗ 19](https://github.com/Atry/memcontinuationed) - Memcached client for Scala.
* [Morpheus ★ 6 ⧗ 6](https://github.com/websudos/morpheus) - Reactive type safe Scala Driver for MySQL/Postgres.
* [Phantom ★ 318 ⧗ 4](https://github.com/websudos/phantom) - Reactive type safe Scala driver for Apache Cassandra.
* **[PostgreSQL and MySQL async ★ 695 ⧗ 0](https://github.com/mauricio/postgresql-async)** - Async database drivers to talk to PostgreSQL and MySQL in Scala.
* [ReactiveCouchbase](http://reactivecouchbase.org/) - Reactive Scala Driver for Couchbase. Also includes a Play plug-in. An official plug-in is also in development.
* **[ReactiveMongo ★ 604 ⧗ 3](https://github.com/ReactiveMongo/ReactiveMongo)** - Reactive Scala Driver for MongoDB.
* [ReactiveNeo ★ 34 ⧗ 15](https://github.com/websudos/reactiveneo) - Reactive type-safe Scala driver for Neo4J.
* [rediscala ★ 447 ⧗ 3](https://github.com/etaty/rediscala) - Non-blocking, Reactive Redis driver for Scala (with Sentinel support)
* [Relate ★ 80 ⧗ 1](https://github.com/lucidsoftware/relate) - Lightweight, blazing-fast database access layer for Scala that abstracts the idiosyncricies of the JDBC while keeping complete control over the SQL.
* [Salat ★ 455 ⧗ 1](https://github.com/salat/salat/) - ORM for MongoDB. A related Play-plugin is also available.
* [Scala ActiveRecord ★ 240 ⧗ 0](https://github.com/aselab/scala-activerecord) - ORM library for scala, inspired by ActiveRecord of Ruby on Rails.
* **[ScalikeJDBC ★ 517 ⧗ 0](https://github.com/scalikejdbc/scalikejdbc)** - A tidy SQL-based DB access library for Scala developers.
* **[Slick ★ 1350 ⧗ 0](https://github.com/slick/slick)** - Modern database query and access library for Scala.
* [Sorm ★ 187 ⧗ 7](https://github.com/sorm/sorm) - A functional boilerplate-free Scala ORM.
* [Squeryl ★ 450 ⧗ 0](https://github.com/squeryl/squeryl) - A Scala DSL for talking with databases with minimum verbosity and maximum type safety.
* [Tepkin ★ 80 ⧗ 2](https://github.com/fehmicansaglam/tepkin) - Reactive MongoDB Driver for Scala built on top of Akka IO and Akka Streams.

## Graphical User Interfaces

*Libraries for creation of graphical user interfaces*

* [ScalaFX](http://www.scalafx.org/) - Scala DSL for creating Graphical User Interfaces that sits on top of JavaFX.

## Web Frameworks

*Scala frameworks for web development.*

* [Chaos ★ 161 ⧗ 4](https://github.com/mesosphere/chaos) - A lightweight framework for writing REST services in Scala.
* [Colossus](http://tumblr.github.io/colossus/) - lightweight framework for building high-performance applications in Scala that require non-blocking network I/O.
* **[Finatra ★ 962 ⧗ 0](https://github.com/twitter/finatra)** - A sinatra-inspired web framework for scala, running on top of Finagle.
* **[Lift ★ 935 ⧗ 2](https://github.com/lift/framework)** - Secure and powerful full stack web framework ([discussion](https://github.com/lauris/awesome-scala/pull/19)).
* **[Play ★ 6934 ⧗ 0](https://github.com/playframework/playframework)** - Makes it easy to build scalable, fast and real-time web applications with Java & Scala.
* [Reactive ★ 189 ⧗ 2](https://github.com/nafg/reactive) - FRP and web abstractions, which can be plugged into any web framework (currently only has bindings for Lift).
* **[Scalatra ★ 1763 ⧗ 0](https://github.com/scalatra/scalatra)** - Tiny Scala high-performance, async web framework, inspired by Sinatra.
* [Skinny Framework ★ 472 ⧗ 0](https://github.com/skinny-framework/skinny-framework) - A full-stack web app framework upon Scalatra for rapid Development in Scala.
* [Socko](http://sockoweb.org/) - An embedded Scala web server powered by Netty networking and Akka processing.
* **[Spray ★ 2088 ⧗ 0](https://github.com/spray/spray)** - A suite of scala libraries for building and consuming RESTful web services on top of Akka.
* **[Unfiltered ★ 609 ⧗ 0](https://github.com/unfiltered/unfiltered)** - A modular set of unopinionated primitives for servicing HTTP and WebSocket requests in Scala.
* [Xitrum](http://xitrum-framework.github.io/) - An async and clustered Scala web framework and HTTP(S) server fusion on top of Netty, Akka, and Hazelcast.

## i18n

*Scala libraries for i18n.*

* [scala-xgettext ★ 13 ⧗ 67](https://github.com/xitrum-framework/scala-xgettext) - A compiler plugin that acts like GNU xgettext command to extract i18n strings in Scala source code files to Gettext .po file.
* [Scaposer ★ 25 ⧗ 9](https://github.com/xitrum-framework/scaposer) - GNU Gettext .po file loader for Scala.

## Authentication

*Libraries for implementing authentications schemes.*

* [play-pac4j ★ 172 ⧗ 40](https://github.com/pac4j/play-pac4j) - Security library managing authentication (CAS, OAuth, OpenID, SAML, LDAP, SQL, JWT...), authorizations and logout for Play 2.x in Java and Scala.
* [play-silhouette ★ 369 ⧗ 4](https://github.com/mohiva/play-silhouette) - Authentication library for Play Framework applications that supports several authentication methods, including OAuth1, OAuth2, OpenID, Credentials or custom authentication schemes.
* **[play2-auth ★ 513 ⧗ 6](https://github.com/t2v/play2-auth)** - Play2.x Authentication and Authorization module.
* [scala-oauth2-provider ★ 252 ⧗ 0](https://github.com/nulab/scala-oauth2-provider) - OAuth 2.0 server-side implementation written in Scala.
* **[SecureSocial ★ 1118 ⧗ 6](https://github.com/jaliss/securesocial)** - A module that provides OAuth, OAuth2 and OpenID authentication for Play Framework applications.

## Authorization

*Libraries for implementing authorization strategies.*

* [deadbolt-2 ★ 363 ⧗ 3](https://github.com/schaloner/deadbolt-2) - A Play 2.x module supporting role-based and proprietary authorization; idiomatic APIs for Scala and Java APIs are provided.

## Testing

*Libraries for code testing.*

* [Gatling](http://gatling-tool.org/) - Async Scala-Akka-Netty based Stress Tool.
* **[ScalaCheck ★ 869 ⧗ 0](https://github.com/rickynils/scalacheck)** - Property-based testing for Scala.
* [ScalaMeter](https://scalameter.github.io/) - Performance &  memory footprint measuring, regression testing.
* [ScalaMock](http://scalamock.org) - Scala native mocking framework
* [ScalaTest ★ 305 ⧗ 2](https://github.com/scalatest/scalatest) - A testing tool for Scala and Java developers.
* [Scalive ★ 120 ⧗ 6](https://github.com/xitrum-framework/scalive) - Connect a Scala REPL to running JVM processes without any prior setup; this library is used for inspecting systems in production mode.
* [Specs2 ★ 468 ⧗ 0](https://github.com/etorreborre/specs2) - Software Specifications for Scala.
* [µTest ★ 124 ⧗ 6](https://github.com/lihaoyi/utest) - A tiny, portable testing library for Scala.
* [scalaprops](https://github.com/scalaprops/scalaprops) - Another property based testing library for Scala
## JSON Manipulation

*Libraries for work with json.*

* [argonaut](http://argonaut.io/) - Purely Functional JSON in Scala.
* [circe ★ 173 ⧗ 4](https://github.com/travisbrown/circe) - JSON library based on Argonaut, depends on Cats
* [jackson-module-scala ★ 229 ⧗ 2](https://github.com/FasterXML/jackson-module-scala) - Add-on module for Jackson to support Scala-specific datatypes.
* **[json4s ★ 542 ⧗ 0](https://github.com/json4s/json4s)** - Project aims to provide a single AST to be used by other scala json libraries.
* [play-json](https://github.com/playframework/playframework/tree/master/framework/src/play-json) - Flexible and powerful JSON manipulation, validation and serialization, with no reflection at runtime.
* [scalajack ★ 64 ⧗ 46](https://github.com/gzoller/ScalaJack) - Fast 'n easy JSON serialization with optional MongoDB support.  Uses Jackson under the hood.
* [spray-json ★ 432 ⧗ 3](https://github.com/spray/spray-json) - Lightweight, clean and efficient JSON implementation in Scala.

## Serialization

*Libraries for serializing and deserializing data for storage or transport.*

* [Chill ★ 301 ⧗ 2](https://github.com/twitter/chill) - Extensions for the Kryo serialization library to ease configuration in systems like Hadoop and Storm.
* **[Pickling ★ 680 ⧗ 0](https://github.com/scala/pickling)** - Fast, customizable, boilerplate-free pickling support.
* [ScalaBuff ★ 181 ⧗ 7](https://github.com/SandroGrzicic/ScalaBuff) - a Scala Protocol Buffers (protobuf) compiler
* [ScalaPB](http://trueaccord.github.io/ScalaPB/) - A Protocol Buffer generator for Scala.
* [scodec ★ 333 ⧗ 1](https://github.com/scodec/scodec) - A combinator library for working with binary data.
* [Scrooge](http://twitter.github.io/scrooge/) - An Apache Thrift code generator for Scala.
* [validation ★ 108 ⧗ 8](https://github.com/jto/validation) - Advanced validation & serialization for JSON, HTML form data, etc, with no reflection at runtime.
* [µPickle](http://lihaoyi.github.io/upickle-pprint/upickle/) - A lightweight serialization library for Scala that works in ScalaJS, allowing transfer of structured data between the JVM and JavaScript.

## Science and Data Analysis

*Libraries for scientific computing, data analysis and numerical processing.*

* **[Algebird ★ 1040 ⧗ 0](https://github.com/twitter/algebird)** - Abstract Algebra for Scala.
* [Axle](http://axle-lang.org) - Spire-based DSL for scientific cloud computing.
* **[Breeze ★ 1210 ⧗ 0](https://github.com/scalanlp/breeze)** - Breeze is a numerical processing library for Scala.
* [Chalk ★ 174 ⧗ 17](https://github.com/scalanlp/chalk) - Chalk is a natural language processing library.
* [FACTORIE ★ 350 ⧗ 1](https://github.com/factorie/factorie) - A toolkit for deployable probabilistic modeling, implemented as a software library in Scala.
* [Figaro ★ 225 ⧗ 1](https://github.com/p2t2/figaro) - Figaro is a probabilistic programming language that supports development of very rich probabilistic models.
* [MGO ★ 9 ⧗ 178](https://github.com/romainreuillon/mgo) - Modular multi-objective evolutionary algorithm optimization library enforcing immutability.
* [MLLib](https://spark.apache.org/mllib/) - Machine Learning framework for Spark
* [OpenMOLE ★ 9 ⧗ 110](https://github.com/ISCPIF/openmole) - OpenMOLE (Open MOdeL Experiment) is a workflow engine designed to leverage the computing power of distributed execution environments for naturally parallel processes.
* [OscaR](https://bitbucket.org/oscarlib/oscar/wiki/Home) - a Scala toolkit for solving Operations Research problems
* **[PredictionIO ★ 7864 ⧗ 0](https://github.com/PredictionIO/PredictionIO)** - machine learning server for developers and data scientists. Built on Apache Spark, HBase and Spray
* [Saddle ★ 340 ⧗ 8](https://github.com/saddle/saddle) - A minimalist port of Pandas to Scala
* **[Spire ★ 802 ⧗ 0](https://github.com/non/spire)** - Powerful new number types and numeric abstractions for Scala.
* [Squants ★ 215 ⧗ 0](https://github.com/garyKeorkunian/squants) - The Scala API for Quantities, Units of Measure and Dimensional Analysis.
* [Zeppelin](http://zeppelin-project.org/) - Scala and Spark Notebook (like IPython Notebook)

## Big Data

* [BIDMach ★ 443 ⧗ 0](https://github.com/BIDData/BIDMach) - CPU and GPU machine learning library, using JNI for GPU computation.
* [Gearpump ★ 342 ⧗ 2](https://github.com/intel-hadoop/gearpump) - Lightweight real-time big data streaming engine
* [GridScale ★ 8 ⧗ 58](https://github.com/romainreuillon/gridscale) - A Scala API for computing clusters and grids.
* **[Scalding ★ 2292 ⧗ 0](https://github.com/twitter/scalding)** - A Scala binding for the Cascading abstraction of Hadoop MapReduce.
* [Scoobi ★ 471 ⧗ 2](https://github.com/nicta/scoobi) - Write type-safe Hadoop programs in idiomatic Scala way
* [Scoozie ★ 52 ⧗ 17](https://github.com/klout/scoozie) - Scala DSL on top of Oozie XML
* [Scrunch](http://crunch.apache.org/scrunch.html) - A Scala wrapper for [Apache Crunch](http://crunch.apache.org/index.html) which provides a framework for writing, testing, and running MapReduce pipelines.
* [Shadoop ★ 8 ⧗ 46](https://github.com/adamretter/shadoop) - A Scala DSL for Hadoop MapReduce.
* [Spark](http://spark.apache.org/) - Lightning fast cluster computing — up to 100x faster than Hadoop for iterative algorithms (memory caching) and up to 10x faster than Hadoop for single-pass MapReduce jobs. Compatible with YARN-enabled Hadoop clusters, can run on Mesos and in stand-alone mode as well.
* [Sparkta](http://github.com/Stratio/sparkta) - Real Time Aggregation based on Spark Streaming.
* **[Summingbird ★ 1566 ⧗ 2](https://github.com/twitter/summingbird)** - An implementation of the “lambda architecture” as a software abstraction — a single API for Hadoop and Storm.

## Image processing and image analysis

*2D and 3D image processing and image analysis*

* [scalismo ★ 14 ⧗ 4](https://github.com/unibas-gravis/scalismo) - Shape modelling and  model-based image analysis.

## Functional Reactive Programming

*Event streams, signals, observables, etc.*

* [Monifu ★ 257 ⧗ 0](https://github.com/monifu/monifu) - Extensions to Scala’s standard library for multi-threading primitives and functional reactive programming. Scala.js compatible.
* [Reactive Collections ★ 79 ⧗ 8](https://github.com/storm-enroute/reactive-collections) - A library that incorporates event streams and signals with specialized collections called reactive containers, and expresses concurrency using isolates and channels.
* [RxScala ★ 336 ⧗ 0](https://github.com/ReactiveX/RxScala) - Reactive Extensions for Scala – a library for composing asynchronous and event-based programs using observable sequences
* [scala.frp ★ 18 ⧗ 67](https://github.com/dylemma/scala.frp) - Functional Reactive Programming for Scala (event streams).
* **[Scala.Rx ★ 550 ⧗ 0](https://github.com/lihaoyi/scala.rx)** - An experimental library for Functional Reactive Programming in Scala (reactive variables). Scala.js compatible.
* [SynapseGrid ★ 75 ⧗ 1](https://github.com/Primetalk/SynapseGrid) - an FRP framework for constructing reactive real-time immutable data flow systems. It implements an original way of running and organizing event-driven systems based on Petri nets. The topology can be viewed as a .dot graph. The library is compatible with Akka and can seamlessly communicate with other actors.
* [Vertx.io](http://vertx.io/) - A polyglot reactive application platform for the JVM which aims to be an alternative to node.js. Its concurrency model resembles actors. It supports [Scala](http://vertx.io/core_manual_scala.html), Clojure, Java, Javascript, Ruby, Groovy and Python.

## Modularization and Dependency Injection

*Modularization of applications, dependency injection, etc.*

* [Domino ★ 0 ⧗ 73](https://github.com/helgoboss/domino) - Write elegant OSGi bundle activators in Scala.
* [MacWire ★ 378 ⧗ 0](https://github.com/adamw/macwire) - Scala Macro to generate wiring code for class instantiation. DI container replacement.
* [Scala-Guice ★ 114 ⧗ 0](https://github.com/codingwell/scala-guice) - Scala extensions for Google Guice
* [Scaldi ★ 182 ⧗ 1](https://github.com/scaldi/scaldi) - Lightweight Scala Dependency Injection Library.
* [Sclasner ★ 7 ⧗ 245](https://github.com/xitrum-framework/sclasner) - Scala classpath scanner.
* [SubCut ★ 381 ⧗ 3](https://github.com/dickwall/subcut) - Scala Uniquely Bound Classes Under Traits.

## Distributed Systems

*Libraries and frameworks for writing distributed applications.*

* [Akka](http://akka.io/) - A toolkit and runtime for building highly concurrent, distributed, and fault tolerant event-driven applications.
* [Clump](http://getclump.io) - A library for expressive and efficient service composition
* [CurioDB ★ 356 ⧗ 5](https://github.com/stephenmcd/curiodb) - Distributed & Persistent Redis Clone built with Scala & Akka.
* [Finagle](https://twitter.github.io/finagle/) - An extensible, protocol-agnostic RPC system designed for high performance and concurrency.
* [Glokka ★ 40 ⧗ 35](https://github.com/xitrum-framework/glokka) - Library to register and lookup actors by names in an Akka cluster.

## Extensions

*Scala extensions.*

* [better-files ★ 317 ⧗ 12](https://github.com/pathikrit/better-files) - Simple, safe and intuitive Scala I/O. better-files is a dependency-free pragmatic thin Scala wrapper around Java NIO.
* **[Cassovary ★ 774 ⧗ 0](https://github.com/twitter/cassovary)** - A Scala library that is designed from the ground up for space efficiency, handling graphs with billions of nodes and edges.
* [Each ★ 47 ⧗ 3](https://github.com/ThoughtWorksInc/each) - A macro library that converts native imperative syntax to [Scalaz](https://github.com/scalaz/scalaz)'s monadic expressions.
* [Lamma ★ 44 ⧗ 3](https://github.com/maxcellent/lamma) - A Scala date library for date and schedule generation.
* [Log4s](http://log4s.org) - Fast, Scala-friendly logging bindings on top of [SLF4J](http://slf4j.org/). Uses macros for extreme performance.
* [Monocle ★ 433 ⧗ 0](https://github.com/julien-truffaut/Monocle) - An Optics/Lens library for purely functional manipulation of immutable objects.
* [Rapture](http://rapture.io/) ([repo](https://github.com/propensive/rapture)) - a collection of libraries for common, everyday programming tasks (I/O, JSON, i18n, etc.)
* [refined ★ 156 ⧗ 0](https://github.com/fthomas/refined) - Simple refinement types with compile- and runtime checking
* [Resolvable ★ 24 ⧗ 51](https://github.com/resolvable/resolvable) - A library to optimize fetching immutable data structures from several endpoints in several formats.
* **[Scala Async ★ 558 ⧗ 0](https://github.com/scala/async)** - An asynchronous programming facility for Scala.
* [Scala Blitz](http://scala-blitz.github.io/) - A library to speed up Scala collection operations by removing runtime overheads during compilation, and a custom data-parallel operation runtime.
* [Scala Graph](http://www.scala-graph.org/) - A Scala library with basic graph functionality that seamlessly fits into the Scala standard collections library.
* [Scalactic](http://www.scalactic.org/) - Small library of utilities related to quality that helps keeping code clear and correct.
* **[Scalaz ★ 2123 ⧗ 0](https://github.com/scalaz/scalaz)** - An extension to the core Scala library for functional programming.
* **[Shapeless ★ 1236 ⧗ 0](https://github.com/milessabin/shapeless)** - A type class and dependent type based generic programming library for Scala.
* [Stateless Future ★ 109 ⧗ 7](https://github.com/qifun/stateless-future) - Asynchronous programming in fully featured Scala syntax.
* **[Twitter Util ★ 1322 ⧗ 0](https://github.com/twitter/util)** - General-purpose Scala libraries, including a future implementation and other concurrency tools.

## Misc

*Projects that don't fit into any specific category.*

* [Ammonite](http://lihaoyi.github.io/Ammonite/) - Ammonite is a collection of Scala libraries intended to improve the experience of using Scala as an system shell.
* [REPLesent ★ 166 ⧗ 2](https://github.com/marconilanna/REPLesent) - A presentation tool built inside the Scala REPL. Runs code straight from your slides with a single keystroke.
* [scala-ssh ★ 139 ⧗ 19](https://github.com/sirthias/scala-ssh) - Remote shell access via SSH for your Scala applications
* [Scalan ★ 36 ⧗ 2](https://github.com/scalan/scalan) - A framework for development of domain-specific compilers in Scala
* [ScalaSTM](https://nbronson.github.io/scala-stm/) - Software Transaction Memory for Scala

## Android

*Scala libraries and wrappers for Android development.*

* [Android SDK Plugin for SBT ★ 383 ⧗ 2](https://github.com/pfn/android-sdk-plugin) - An sbt plugin that adds tasks for developing Android applications.
* [Gradle Android Scala Plugin ★ 227 ⧗ 0](https://github.com/saturday06/gradle-android-scala-plugin) - A gradle plugin that allows you to use Scala with Android
* [Macroid ★ 307 ⧗ 5](https://github.com/macroid/macroid) - A modular functional UI language for Android.
* **[Scaloid ★ 1775 ⧗ 0](https://github.com/pocorall/scaloid)** - Less painful Android development with Scala.

## HTTP

*Scala libraries and wrappers for HTTP clients.*

* [Dispatch ★ 308 ⧗ 2](https://github.com/dispatch/reboot) - Library for asynchronous HTTP interaction. It provides a Scala vocabulary for Java’s [async-http-client](https://github.com/AsyncHttpClient/async-http-client).
* [Finch.io ★ 449 ⧗ 0](https://github.com/finagle/finch) - Purely Functional REST API atop of [Finagle](https://github.com/twitter/finagle).
* [Http4s ★ 321 ⧗ 3](https://github.com/http4s/http4s) - A minimal, idiomatic Scala interface for HTTP.
* [Netcaty ★ 9 ⧗ 112](https://github.com/ngocdaothanh/netcaty) - Simple net test client/server for Netty and Scala lovers.
* [Newman ★ 221 ⧗ 0](https://github.com/stackmob/newman) - A REST DSL that tries to take the best from Dispatch, Finagle and Apache HttpClient. See [here](https://www.paypal-engineering.com/2014/02/13/hello-newman-a-rest-client-for-scala/) for rationale.
* [scalaj-http ★ 313 ⧗ 1](https://github.com/scalaj/scalaj-http) - Simple scala wrapper for HttpURLConnection (including OAuth support).
* [Scalaxb ★ 180 ⧗ 11](https://github.com/eed3si9n/scalaxb) - An XML data-binding tool for Scala that supports W3C XML Schema (xsd) and Web Services Description Language (wsdl) as the input file.
* [Spray](http://spray.io/) - Actor-based library for http interaction.
* [Tubesocks ★ 7 ⧗ 456](https://github.com/softprops/tubesocks) - Library supporting bi-directional communication with websocket servers.

## Semantic Web

*Scala libraries for interactions with the Web of Data, and other RDF tools.*

* [Banana-RDF ★ 167 ⧗ 0](https://github.com/w3c/banana-rdf) - Scala-friendly abstractions for RDF and Linked Data technologies. Supports Jena, Sesame and native Scala.
* [rdfp](https://github.com/jannvck/rdfp) - RDF stream processing framework in Scala

## Metrics and Monitoring

*Scala libraries for gathering metrics and monitoring applications.*

* [Kamon](http://kamon.io) - Gathering metrics from applications built with Akka, Spray and Play! with support for user metrics as well.

## Parsing

*Scala libraries for creating parsers.*

* [atto ★ 96 ⧗ 0](https://github.com/tpolecat/atto) - Pure functional incremental text parsing library for Scala, based on Attoparsec.
* [Parboiled2 ★ 372 ⧗ 0](https://github.com/sirthias/parboiled2) - A Fast Parser Generator for Scala 2.10.3+.
* [Scala Parser Combinators ★ 94 ⧗ 0](https://github.com/scala/scala-parser-combinators) - Scala Standard Parser Combinator Library.

## Sbt plugins

*Sbt plugins to make your life easier.*

* [pttrt ★ 1 ⧗ 154](https://github.com/Atry/pttrt) - A sbt plugin, designed to pass data from compile-time to run-time.
* [sbt-api-mappings ★ 24 ⧗ 4](https://github.com/ThoughtWorksInc/sbt-api-mappings) - A Sbt plugin that resolves external API links to common Scala libraries.
* [sbt-buildinfo ★ 163 ⧗ 15](https://github.com/sbt/sbt-buildinfo) - Generates Scala source from build definition.
* [sbt-cppp ★ 1 ⧗ 79](https://github.com/Atry/sbt-cppp) - A sbt plugin to support [Protocol Buffers](https://github.com/google/protobuf), especially in multi-project builds.
* [sbt-dependency-graph ★ 399 ⧗ 1](https://github.com/jrudolph/sbt-dependency-graph) - Create a dependency graph for your project.
* [sbt-haxe ★ 6 ⧗ 7](https://github.com/qifun/sbt-haxe) - A Sbt plugin to compile Haxe sources.
* [sbt-ide-settings ★ 17 ⧗ 53](https://github.com/Jetbrains/sbt-ide-settings) - SBT plugin for tweaking various IDE settings
* [sbt-native-packager ★ 478 ⧗ 0](https://github.com/sbt/sbt-native-packager) - Bundle up Scala software for native packaging systems, like deb, rpm, homebrew, msi..
* [sbt-pack ★ 190 ⧗ 0](https://github.com/xerial/sbt-pack) - A sbt plugin for creating distributable Scala packages.
* [sbt-revolver ★ 380 ⧗ 0](https://github.com/spray/sbt-revolver) - Fork & Stop processes from sbt.
* [sbt-robovm ★ 91 ⧗ 8](https://github.com/roboscala/sbt-robovm) - An sbt plugin for iOS development in Scala
* [sbt-sublime ★ 115 ⧗ 21](https://github.com/orrsella/sbt-sublime) - Create Sublime Text projects with library dependencies sources
* [sbt-updates ★ 208 ⧗ 0](https://github.com/rtimush/sbt-updates) - Shows sbt project's dependency updates.
* [sbt-versions ★ 8 ⧗ 80](https://github.com/sksamuel/sbt-versions) - Plugin that checks for updated versions of your project's dependencies.
* **[sbteclipse ★ 510 ⧗ 0](https://github.com/typesafehub/sbteclipse)** - Create Eclipse project definitions from sbt builds.
* [ScalaKata2 ★ 7 ⧗ 25](https://github.com/MasseGuillaume/ScalaKata2) - Scala playground & Documentation tool.
* [tut ★ 143 ⧗ 0](https://github.com/tpolecat/tut) - Tool for writing documentation with typechecked examples.
* [xsbt-web-plugin ★ 298 ⧗ 10](https://github.com/earldouglas/xsbt-web-plugin) - Build enterprise J2EE Web applications in Scala.

## XML / HTML

*Xml and Html generation and processing*

* [Scalatags ★ 335 ⧗ 0](https://github.com/lihaoyi/scalatags) - Write html as scala code and have your ide syntax check it.

## Learning Scala

*Nice books, blogs and other resources to learn Scala*

* [Scala Exercises](http://scala-exercises.47deg.com/) - None
* [Scala in Depth](http://www.manning.com/suereth/) - None
* [The Neophyte's Guide to Scala](http://danielwestheide.com/scala/neophytes.html) - None

## JavaScript

*JavaScript generation and interop libraries.*

* [js-scala ★ 148 ⧗ 61](https://github.com/js-scala/js-scala) - JavaScript as an embedded DSL in Scala
* [scala-js-fiddle](http://www.scala-js-fiddle.com/) ([repo](https://github.com/lihaoyi/scala-js-fiddle)) - Browser-based Scala.js playground
* [Scala.js](http://www.scala-js.org/) ([repo](https://github.com/scala-js/scala-js)) - Scala to JavaScript compiler

## Tools

* [Abide ★ 187 ⧗ 2](https://github.com/scala/scala-abide) - Library for quick scala code checking and validation
* [Codacy](https://www.codacy.com/) - Automated Code Reviews for Scala
* **[Gitbucket ★ 4722 ⧗ 0](https://github.com/takezoe/gitbucket)** - The easily installable GitHub clone powered by Scala
* [sbt](http://www.scala-sbt.org/) ([repo](https://github.com/sbt/sbt)) - The interactive build tool for Scala
* [Scalariform ★ 95 ⧗ 1](https://github.com/daniel-trinh/scalariform) - Scala source code formatter
* [Scalatex ★ 160 ⧗ 14](https://github.com/lihaoyi/Scalatex) - Programmable, Typesafe Document Generation
* [Scalastyle ★ 320 ⧗ 0](https://github.com/scalastyle/scalastyle) - Scala style checker.
* [Scapegoat ★ 102 ⧗ 1](https://github.com/sksamuel/scalac-scapegoat-plugin) - Scala compiler plugin for static code analysis
* [Scaps](http://scala-search.org/) ([repo](https://github.com/scala-search/scaps)) - A search engine for Scala libraries
* [Scoverage](https://github.com/scoverage) - Scala Code Coverage tool
* [Wartremover ★ 386 ⧗ 0](https://github.com/puffnfresh/wartremover) - Wartremover a flexible Scala code linting tool

# Contributing

Your contributions are always welcome! Please submit a pull request or create an issue to add a new framework, library or software to the list. Do not submit a project that hasn’t been updated in the past 6 months or is not awesome.
