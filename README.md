Awesome Scala
=============

A community driven list of useful Scala libraries, frameworks and software. This is not a catalog of all the libraries, just a starting point for your explorations. Inspired by [awesome-python](https://github.com/vinta/awesome-python). Other amazingly awesome lists can be found in the [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) list.

- [Awesome Scala](#awesome-scala)
    - [Database](#database)
    - [Graphical User Interfaces](#graphical-user-interfaces)
    - [Web Frameworks](#web-frameworks)
    - [i18n](#i18n)
    - [Authentication](#authentication)
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

* [Activate](https://github.com/fwbrasil/activate) — Pluggable object persistence in Scala.
* [Elastic4s](https://github.com/sksamuel/elastic4s) - A scala DSL / reactive client for Elasticsearch
* [Phantom](https://github.com/websudos/phantom) — Reactive type safe Scala driver for Apache Cassandra.
* [ReactiveNeo](https://github.com/websudos/reactiveneo) - Reactive type-safe Scala driver for Neo4J.
* [PostgreSQL and MySQL async](https://github.com/mauricio/postgresql-async) — Async database drivers to talk to PostgreSQL and MySQL in Scala.
* [ReactiveCouchbase](http://reactivecouchbase.org/) — Reactive Scala Driver for Couchbase. Also includes a Play plug-in. An official plug-in is also in development.
* [ReactiveMongo](https://github.com/ReactiveMongo/ReactiveMongo) — Reactive Scala Driver for MongoDB.
* [Salat](https://github.com/novus/salat/) — ORM for MongoDB. A related Play-plugin is also available.
* [Scala ActiveRecord](https://github.com/aselab/scala-activerecord) — ORM library for scala, inspired by ActiveRecord of Ruby on Rails.
* [ScalikeJDBC](https://github.com/scalikejdbc/scalikejdbc) — A tidy SQL-based DB access library for Scala developers.
* [Slick](https://github.com/slick/slick) — Modern database query and access library for Scala.
* [Sorm](https://github.com/sorm/sorm) — A functional boilerplate-free Scala ORM.
* [Squeryl](https://github.com/squeryl/squeryl) — A Scala DSL for talking with databases with minimum verbosity and maximum type safety.
* [doobie](https://github.com/tpolecat/doobie) - Pure functional JDBC layer for Scala.
* [MapperDao](https://github.com/kostaskougios/mapperdao) - An ORM library for oracle, mysql, mssql, and postgresql
* [Tepkin](https://github.com/fehmicansaglam/tepkin) — Reactive MongoDB Driver for Scala built on top of Akka IO and Akka Streams.
* [Casbah](http://mongodb.github.io/casbah/) ([repo](https://github.com/mongodb/casbah)) - Officially supported Scala driver for MongoDB
* [rediscala](https://github.com/etaty/rediscala) - Non-blocking, Reactive Redis driver for Scala (with Sentinel support)

## Graphical User Interfaces

*Libraries for creation of graphical user interfaces*

* [ScalaFX](http://www.scalafx.org/) - Scala DSL for creating Graphical User Interfaces that sits on top of JavaFX.

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
* [Colossus](http://tumblr.github.io/colossus/) — lightweight framework for building high-performance applications in Scala that require non-blocking network I/O.
* [Socko](http://sockoweb.org/) — An embedded Scala web server powered by Netty networking and Akka processing.

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
* [play-silhouette](https://github.com/mohiva/play-silhouette) — Authentication library for Play Framework applications that supports several authentication methods, including OAuth1, OAuth2, OpenID, Credentials or custom authentication schemes.

## Testing

*Libraries for code testing.*

* [ScalaCheck](https://github.com/rickynils/scalacheck) — Property-based testing for Scala.
* [ScalaTest](https://github.com/scalatest/scalatest) — A testing tool for Scala and Java developers.
* [ScalaMeter](https://scalameter.github.io/) - Performance &  memory footprint measuring, regression testing.
* [Specs2](https://github.com/etorreborre/specs2) — Software Specifications for Scala.
* [µTest](https://github.com/lihaoyi/utest) — A tiny, portable testing library for Scala.
* [Scalive](https://github.com/xitrum-framework/scalive) — Connect a Scala REPL to running JVM processes without any prior setup; this library is used for inspecting systems in production mode.
* [Gatling](http://gatling-tool.org/) – Async Scala-Akka-Netty based Stress Tool.
* [ScalaMock](http://scalamock.org) – Scala native mocking framework

## JSON Manipulation

*Libraries for work with json.*

* [json4s](https://github.com/json4s/json4s) — Project aims to provide a single AST to be used by other scala json libraries.
* [spray-json](https://github.com/spray/spray-json) — Lightweight, clean and efficient JSON implementation in Scala.
* [argonaut](http://argonaut.io/) — Purely Functional JSON in Scala.
* [jackson-module-scala](https://github.com/FasterXML/jackson-module-scala) — Add-on module for Jackson to support Scala-specific datatypes.
* [play-json](https://github.com/playframework/playframework/tree/master/framework/src/play-json) — Flexible and powerful JSON manipulation, validation and serialization, with no reflection at runtime.
* [scalajack](https://github.com/gzoller/ScalaJack) - Fast 'n easy JSON serialization with optional MongoDB support.  Uses Jackson under the hood.

## Serialization

*Libraries for serializing and deserializing data for storage or transport.*

* [Pickling](https://github.com/scala/pickling) — Fast, customizable, boilerplate-free pickling support.
* [scodec](https://github.com/scodec/scodec) — A combinator library for working with binary data.
* [Scrooge](http://twitter.github.io/scrooge/) — An Apache Thrift code generator for Scala.
* [validation](https://github.com/jto/validation) — Advanced validation & serialization for JSON, HTML form data, etc, with no reflection at runtime.
* [Chill](https://github.com/twitter/chill) — Extensions for the Kryo serialization library to ease configuration in systems like Hadoop and Storm.
* [µPickle](http://lihaoyi.github.io/upickle-pprint/upickle/) — A lightweight serialization library for Scala that works in ScalaJS, allowing transfer of structured data between the JVM and JavaScript.
* [ScalaPB](http://trueaccord.github.io/ScalaPB/) - A Protocol Buffer generator for Scala.
* [ScalaBuff](https://github.com/SandroGrzicic/ScalaBuff) - a Scala Protocol Buffers (protobuf) compiler

## Science and Data Analysis

*Libraries for scientific computing, data analysis and numerical processing.*

* [Algebird](https://github.com/twitter/algebird) — Abstract Algebra for Scala.
* [Axle](http://axle-lang.org) — Spire-based DSL for scientific cloud computing.
* [Breeze](https://github.com/scalanlp/breeze) — Breeze is a numerical processing library for Scala.
* [Chalk](https://github.com/scalanlp/chalk) — Chalk is a natural language processing library.
* [FACTORIE](https://github.com/factorie/factorie) — A toolkit for deployable probabilistic modeling, implemented as a software library in Scala.
* [Figaro](https://github.com/p2t2/figaro) - Figaro is a probabilistic programming language that supports development of very rich probabilistic models.
* [MGO](https://github.com/romainreuillon/mgo) — Modular multi-objective evolutionary algorithm optimization library enforcing immutability.
* [MLLib](https://spark.apache.org/mllib/) — Machine Learning framework for Spark
* [OpenMOLE](https://github.com/ISCPIF/openmole) — OpenMOLE (Open MOdeL Experiment) is a workflow engine designed to leverage the computing power of distributed execution environments for naturally parallel processes.
* [Saddle](https://github.com/saddle/saddle) — A minimalist port of Pandas to Scala
* [Spire](https://github.com/non/spire) — Powerful new number types and numeric abstractions for Scala.
* [Squants](https://github.com/garyKeorkunian/squants) — The Scala API for Quantities, Units of Measure and Dimensional Analysis.
* [PredictionIO](https://github.com/PredictionIO/PredictionIO) - machine learning server for developers and data scientists. Built on Apache Spark, HBase and Spray
* [OscaR](https://bitbucket.org/oscarlib/oscar/wiki/Home) - a Scala toolkit for solving Operations Research problems

## Big Data

* [Spark](http://spark.apache.org/) — Lightning fast cluster computing — up to 100x faster than Hadoop for iterative algorithms (memory caching) and up to 10x faster than Hadoop for single-pass MapReduce jobs. Compatible with YARN-enabled Hadoop clusters, can run on Mesos and in stand-alone mode as well.
* [Scalding](https://github.com/twitter/scalding) — A Scala binding for the Cascading abstraction of Hadoop MapReduce.
* [Summingbird](https://github.com/twitter/summingbird) — An implementation of the “lambda architecture” as a software abstraction — a single API for Hadoop and Storm.
* [Shadoop](https://github.com/adamretter/shadoop) - A Scala DSL for Hadoop MapReduce.
* [Scrunch](http://crunch.apache.org/scrunch.html) — A Scala wrapper for [Apache Crunch](http://crunch.apache.org/index.html) which provides a framework for writing, testing, and running MapReduce pipelines.
* [GridScale](https://github.com/romainreuillon/gridscale) — A Scala API for computing clusters and grids.
* [BIDMach](https://github.com/BIDData/BIDMach) - CPU and GPU machine learning library, using JNI for GPU computation.
* [scoozie](https://github.com/klout/scoozie) — Scala DSL on top of Oozie XML.
* [Scoobi] (https://github.com/nicta/scoobi) - Write type-safe Hadoop programs in idiomatic Scala way
* [Gearpump](https://github.com/intel-hadoop/gearpump) - Lightweight real-time big data streaming engine
* [Scoozie](https://github.com/klout/scoozie) - Scala DSL on top of Oozie XML

## Image processing and image analysis

*2D and 3D image processing and image analysis*

* [scalismo](https://github.com/unibas-gravis/scalismo) - Shape modelling and  model-based image analysis.

## Functional Reactive Programming

*Event streams, signals, observables, etc.*

* [Scala.Rx](https://github.com/lihaoyi/scala.rx) — An experimental library for Functional Reactive Programming in Scala (reactive variables). Scala.js compatible.
* [scala.frp](https://github.com/dylemma/scala.frp) — Functional Reactive Programming for Scala (event streams).
* [RxScala](https://github.com/ReactiveX/RxScala) — Reactive Extensions for Scala – a library for composing asynchronous and event-based programs using observable sequences
* [Reactive Collections](https://github.com/storm-enroute/reactive-collections) – A library that incorporates event streams and signals with specialized collections called reactive containers, and expresses concurrency using isolates and channels.
* [Vertx.io](http://vertx.io/) – A polyglot reactive application platform for the JVM which aims to be an alternative to node.js. Its concurrency model resembles actors. It supports [Scala](http://vertx.io/core_manual_scala.html), Clojure, Java, Javascript, Ruby, Groovy and Python.
* [Monifu](https://github.com/monifu/monifu) — Extensions to Scala’s standard library for multi-threading primitives and functional reactive programming. Scala.js compatible.

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
* [CurioDB](https://github.com/stephenmcd/curiodb) - Distributed & Persistent Redis Clone built with Scala & Akka.

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
* [Scala Graph](http://www.scala-graph.org/) – A Scala library with basic graph functionality that seamlessly fits into the Scala standard collections library.
* [Cassovary](https://github.com/twitter/cassovary) – A Scala library that is designed from the ground up for space efficiency, handling graphs with billions of nodes and edges.
* [Scalactic](http://www.scalactic.org/) - Small library of utilities related to quality that helps keeping code clear and correct.
* [Monocle](https://github.com/julien-truffaut/Monocle) - An Optics/Lens library for purely functional manipulation of immutable objects.
* [Rapture](http://rapture.io/) ([repo](https://github.com/propensive/rapture)) - a collection of libraries for common, everyday programming tasks (I/O, JSON, i18n, etc.)

## Misc

*Projects that don't fit into any specific category.*

* [REPLesent](https://github.com/marconilanna/REPLesent) – A presentation tool built inside the Scala REPL. Runs code straight from your slides with a single keystroke.
* [ScalaSTM](https://nbronson.github.io/scala-stm/) - Software Transaction Memory for Scala
* [scala-ssh](https://github.com/sirthias/scala-ssh) - Remote shell access via SSH for your Scala applications

## Android

*Scala libraries and wrappers for Android development.*

* [Scaloid](https://github.com/pocorall/scaloid) — Less painful Android development with Scala.
* [Macroid](https://github.com/macroid/macroid) — A modular functional UI language for Android.
* [Android SDK Plugin for SBT](https://github.com/pfn/android-sdk-plugin) — An sbt plugin that adds tasks for developing Android applications.
* [Gradle Android Scala Plugin](https://github.com/saturday06/gradle-android-scala-plugin) - A gradle plugin that allows you to use Scala with Android

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

*Scala libraries for interactions with the Web of Data, and other RDF tools.*

* [Banana-RDF](https://github.com/w3c/banana-rdf) – Scala-friendly abstractions for RDF and Linked Data technologies. Supports Jena, Sesame and native Scala.

## Metrics and Monitoring

*Scala libraries for gathering metrics and monitoring applications.*

* [Kamon](http://kamon.io) - Gathering metrics from applications built with Akka, Spray and Play! with support for user metrics as well.

## Parsing

*Scala libraries for creating parsers.*

* [Scala Parser Combinators](https://github.com/scala/scala-parser-combinators) – Scala Standard Parser Combinator Library.
* [Parboiled2](https://github.com/sirthias/parboiled2) – A Fast Parser Generator for Scala 2.10.3+.
* [atto](https://github.com/tpolecat/atto) - Pure functional incremental text parsing library for Scala, based on Attoparsec.

## Sbt plugins

*Sbt plugins to make your life easier.*

* [Sbt-Revolver](https://github.com/spray/sbt-revolver) – Fork & Stop processes from sbt.
* [Sbt-Eclipse](https://github.com/typesafehub/sbteclipse) – Create Eclipse project definitions from sbt builds.
* [Sbt-Idea](https://github.com/mpeltonen/sbt-idea) – Create IntelliJ IDEA project definitions from sbt builds (not needed from IntelliJ 14, it supports sbt/scala projects through the Scala plugin).
* [Sbt-Native-Packager](https://github.com/sbt/sbt-native-packager) – Bundle up Scala software for native packaging systems, like deb, rpm, homebrew, msi..
* [Sbt-Dependency-Graph](https://github.com/jrudolph/sbt-dependency-graph) – Create a dependency graph for your project.
* [Sbt-Versions](https://github.com/sksamuel/sbt-versions) - Plugin that checks for updated versions of your project's dependencies.
* [Sbt-One-Jar](https://github.com/sbt/sbt-onejar) – Packages your project using One-JAR™.
* [Sbt-Start-Script](https://github.com/sbt/sbt-start-script) – Create a "start" script to run the program.
* [Sbt-Sublime](https://github.com/orrsella/sbt-sublime) – Create Sublime Text projects with library dependencies sources
* [ScalaKata2](https://github.com/MasseGuillaume/ScalaKata2) – Scala playground & Documentation tool.
* [Zeppelin](http://zeppelin-project.org/) - Scala and Spark Notebook (like IPython Notebook)
* [xsbt-web-plugin](https://github.com/earldouglas/xsbt-web-plugin) – Build enterprise J2EE Web applications in Scala.
* [tut](https://github.com/tpolecat/tut) - Tool for writing documentation with typechecked examples.
* [sbt-ide-settings](https://github.com/Jetbrains/sbt-ide-settings) - SBT plugin for tweaking various IDE settings
* [Sbt-BuildInfo](https://github.com/sbt/sbt-buildinfo) – Generates Scala source from build definition.
* [Sbt-Updates](https://github.com/rtimush/sbt-updates) – Shows sbt project's dependency updates.
* [sbt-pack](https://github.com/xerial/sbt-pack) - A sbt plugin for creating distributable Scala packages.
* [Ammonite](http://lihaoyi.github.io/Ammonite/) - Ammonite is a collection of Scala libraries intended to improve the experience of using Scala as an system shell.
* [sbt-robovm](https://github.com/roboscala/sbt-robovm) - An sbt plugin for iOS development in Scala

## XML / HTML

*Xml and Html generation and processing*

* [Scalatags](https://github.com/lihaoyi/scalatags) - Write html as scala code and have your ide syntax check it.

## Learning Scala

*Nice books, blogs and other resources to learn Scala*

* [The Neophyte's Guide to Scala](http://danielwestheide.com/scala/neophytes.html)
* [Scala in Depth](http://www.manning.com/suereth/)
* [Scala Exercises](http://scala-exercises.47deg.com/)

## JavaScript

*JavaScript generation and interop libraries.*

* [Scala.js](http://www.scala-js.org/) ([repo](https://github.com/scala-js/scala-js)) - Scala to JavaScript compiler
* [js-scala](https://github.com/js-scala/js-scala) - JavaScript as an embedded DSL in Scala
* [scala-js-fiddle](http://www.scala-js-fiddle.com/) ([repo](https://github.com/lihaoyi/scala-js-fiddle)) - Browser-based Scala.js playground

## Tools

* [sbt](http://www.scala-sbt.org/) ([repo](https://github.com/sbt/sbt)) - The interactive build tool for Scala
* [Scalastyle](https://github.com/scalastyle/scalastyle) – Scala style checker.
* [Codacy](https://www.codacy.com/) - Automated Code Reviews for Scala
* [Wartremover](https://github.com/puffnfresh/wartremover) - Wartremover a flexible Scala code linting tool
* [Abide](https://github.com/scala/scala-abide) - Library for quick scala code checking and validation
* [Scoverage](https://github.com/scoverage) - Scala Code Coverage tool
* [Gitbucket](https://github.com/takezoe/gitbucket) - The easily installable GitHub clone powered by Scala
* [Scapegoat](https://github.com/sksamuel/scalac-scapegoat-plugin) - Scala compiler plugin for static code analysis
* [Scalariform](https://github.com/daniel-trinh/scalariform) - Scala source code formatter

# Contributing

Your contributions are always welcome! Please submit a pull request or create an issue to add a new framework, library or software to the list. Do not submit a project that hasn’t been updated in the past 6 months or is not awesome.
