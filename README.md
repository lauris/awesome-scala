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
    - [Extensions](#extensions)
    - [Android](#android)
    - [HTTP](#http)
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

## Web Frameworks

*Scala frameworks for web development.*

* [Play](https://github.com/playframework/playframework) — Makes it easy to build scalable, fast and real-time web applications with Java & Scala.
* [Skinny Framework](https://github.com/skinny-framework/skinny-framework) — A full-stack web app framework upon Scalatra for rapid Development in Scala.
* [Scalatra](https://github.com/scalatra/scalatra) — Tiny Scala high-performance, async web framework, inspired by Sinatra.
* [Spray](https://github.com/spray/spray) — A suite of scala libraries for building and consuming RESTful web services on top of Akka.
* [Finatra](https://github.com/twitter/finatra) — A sinatra-inspired web framework for scala, running on top of Finagle.
* [Reactive](https://github.com/nafg/reactive) — FRP and web abstractions, which can be plugged into any web framework (currently only has bindings for Lift).
* [Chaos](https://github.com/mesosphere/chaos) — A lightweight framework for writing REST services in Scala.
* [Xitrum](http://xitrum-framework.github.io/) — An async and clustered Scala web framework and HTTP(S) server fusion on top of Netty, Akka, and Hazelcast.
* [Unfiltered](https://github.com/unfiltered/unfiltered) — An modular set of unopinionated primitives for servicing HTTP and WebSocket requests in Scala.


## i18n

*Scala libraries for i18n.*

* [Scaposer](https://github.com/xitrum-framework/scaposer) - GNU Gettext .po file loader for Scala.
* [scala-xgettext](https://github.com/xitrum-framework/scala-xgettext) - A compiler plugin that acts like GNU xgettext command to extract i18n strings in Scala source code files to Gettext .po file.

## Authentication

*Libraries for implementing authentications schemes.*

* [scala-oauth2-provider](https://github.com/nulab/scala-oauth2-provider) — OAuth 2.0 server-side implementation written in Scala.
* [SecureSocial](https://github.com/jaliss/securesocial) — A module that provides OAuth, OAuth2 and OpenID authentication for Play Framework applications.
* [play2-auth](https://github.com/t2v/play2-auth) — Play2.x Authentication and Authorization module.
* [play-pac4j](https://github.com/leleuj/play-pac4j) — Profile & Authentication Client in Scala (and Java) for CAS, OAuth, OpenID, SAML, HTTP... protocols and Play 2.x framework.

## Testing

*Libraries for code testing.*

* [ScalaCheck](https://github.com/rickynils/scalacheck) — Property-based testing for Scala.
* [ScalaTest](https://github.com/scalatest/scalatest) — A testing tool for Scala and Java developers.
* [Specs2](https://github.com/etorreborre/specs2) — Software Specifications for Scala.
* [µTest](https://github.com/lihaoyi/utest) — A tiny, portable testing library for Scala.
* [Scalive](https://github.com/xitrum-framework/scalive) — Connect a Scala REPL to running JVM processes without any prior setup; this library is used for inspecting systems in production mode.

## JSON Manipulation

*Libraries for work with json.*

* [json4s](https://github.com/json4s/json4s) — Project aims to provide a single AST to be used by other scala json libraries.
* [spray-json](https://github.com/spray/spray-json) — Lightweight, clean and efficient JSON implementation in Scala.
* [argonaut](http://argonaut.io/) — Purely Functional JSON in Scala.
* [jackson-module-scala](https://github.com/FasterXML/jackson-module-scala) — Add-on module for Jackson to support Scala-specific datatypes.
* [play-json](https://github.com/playframework/playframework/tree/master/framework/src/play-json) — Flexible and powerful JSON manipulation, validation and serialization, with no reflection at runtime ([docs](http://www.playframework.com/documentation/2.2.x/ScalaJson), published separately at `"com.typesafe.play" %% "play-json" % playVersion`).

## Serialization

*Libraries for serializing and deserializing data for storage or transport.*

* [Pickling](https://github.com/scala/pickling) — Fast, customizable, boilerplate-free pickling support.
* [scodec](https://github.com/scodec/scodec) — A combinator library for working with binary data.
* [Scrooge](http://twitter.github.io/scrooge/) — An Apache Thrift code generator for Scala.
* [validation](https://github.com/jto/validation) — Advanced validation & serialization for JSON, HTML form data, etc, with no reflection at runtime ([intro](http://jto.github.io/articles/play_new_validation_api/)).

## Science and Data Analysis

*Libraries for scientific computing, data analysis and numerical processing.*

* [Breeze](https://github.com/scalanlp/breeze) — Breeze is a numerical processing library for Scala.
* [MLLib](https://spark.apache.org/mllib/) — Machine Learning framework for Spark
* [Spire](https://github.com/non/spire) — Powerful new number types and numeric abstractions for Scala.
* [Algebird](https://github.com/twitter/algebird) — Abstract Algebra for Scala.
* [FACTORIE](https://github.com/factorie/factorie) — A toolkit for deployable probabilistic modeling, implemented as a software library in Scala.
* [Saddle](https://github.com/saddle/saddle) — A minimalist port of Pandas to Scala
* [Squants](https://github.com/garyKeorkunian/squants) — The Scala API for Quantities, Units of Measure and Dimensional Analysis.
* [MGO](https://github.com/romainreuillon/mgo) — Modular multi-objective evolutionary algorithm optimization library enforcing immutability.

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

## Modularization and Dependency Injection

*Modularization of applications, dependency injection, etc.*

* [Domino](https://github.com/helgoboss/domino) — Write elegant OSGi bundle activators in Scala.
* [Sclasner](https://github.com/xitrum-framework/sclasner) - Scala classpath scanner.
* [Scaldi](https://github.com/scaldi/scaldi) — Lightweight Scala Dependency Injection Library.
* [MacWire](https://github.com/adamw/macwire) — Scala Macro to generate wiring code for class instantiation. DI container replacement.
* [SubCut](https://github.com/dickwall/subcut) — Scala Uniquely Bound Classes Under Traits.

## Extensions

*Scala extensions.*

* [Scalaz](https://github.com/scalaz/scalaz) — An extension to the core Scala library for functional programming.
* [Shapeless](https://github.com/milessabin/shapeless) — A type class and dependent type based generic programming library for Scala.
* [Twitter Util](https://github.com/twitter/util) — General-purpose Scala libraries, including a future implementation and other concurrency tools.
* [Scala Async](https://github.com/scala/async) — An asynchronous programming facility for Scala.
* [Resolvable](https://github.com/resolvable/resolvable) — A library to optimize fetching immutable data structures from several endpoints in several formats.

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


# Contributing

Your contributions are always welcome! Please submit a pull request or create an issue to add a new framework, library or software to the list. Do not submit a project that hasn’t been updated in the past 6 months or is not awesome.
