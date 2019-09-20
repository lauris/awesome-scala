
Awesome Scala [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
=============

A community driven list of useful Scala libraries, frameworks and software. This is not a catalog of all the libraries, just a starting point for your explorations. Inspired by [awesome-python](https://github.com/vinta/awesome-python). Other amazingly awesome lists can be found in the [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) list.

Also awesome is [Scaladex](https://index.scala-lang.org/), the searchable, tagged, and centralized index of Scala libraries.

Projects with over 500 stargazers are in bold.

## Table of Contents

- [Learning Scala](#learning-scala)
- [Projects](#projects)
    - [Android](#android)
    - [Artificial Intelligence](#artificial-intelligence)
    - [Authentication](#authentication)
    - [Authorization](#authorization)
    - [Big Data](#big-data)
    - [Cryptography](#cryptography)
    - [CSV](#csv)
    - [Data Binding and Validation](#data-binding-and-validation)
    - [Database](#database)
    - [DevOps](#devops)
    - [Distributed Systems](#distributed-systems)
    - [Extensions](#extensions)
    - [Functional Reactive Programming](#functional-reactive-programming)
    - [Geospatial](#geospatial)
    - [Graphical User Interfaces](#graphical-user-interfaces)
    - [HTTP](#http)
    - [i18n](#i18n)
    - [Image processing and image analysis](#image-processing-and-image-analysis)
    - [JavaScript](#javascript)
    - [JSON](#json)
    - [Markdown](#markdown)
    - [Metrics and Monitoring](#metrics-and-monitoring)
    - [Misc](#misc)
    - [Modularization and Dependency Injection](#modularization-and-dependency-injection)
    - [Parsing](#parsing)
    - [Reactive Web Frameworks](#reactive-web-frameworks)
    - [Sbt plugins](#sbt-plugins)
    - [Science and Data Analysis](#science-and-data-analysis)
    - [Scheduling](#scheduling)
    - [Semantic Web](#semantic-web)
    - [Serialization](#serialization)
    - [Templating](#templating)
    - [Testing](#testing)
    - [Tools](#tools)
    - [Web Frameworks](#web-frameworks)
    - [XML / HTML](#xml--html)
    - [YAML](#yaml)
- [Resources](#resources)
    - [Newsletters](#newsletters)
    - [Podcasts](#podcasts)
- [Contributing](#contributing)

## Artificial Intelligence

* [CIlib ★ 82](https://github.com/cirg-up/cilib) - Typesafe, purely functional Computational Intelligence.
* [CIlib-tutorial ★ 2](https://github.com/cirg-up/cilib-tutorial) - A tutorial book for cilib.

## Database

*Database access libraries in Scala.*

* [Anorm ★ 135](https://github.com/playframework/anorm) - Simple SQL data access.
* [Casbah](http://mongodb.github.io/casbah/) ([repo](https://github.com/mongodb/casbah)) - Officially supported Scala driver for MongoDB
* [Clickhouse-scala-client](https://github.com/crobox/clickhouse-scala-client) - Reactive client for Clickhouse
* [CouchDB-Scala ★ 59 ⧗ 21](https://github.com/beloglazov/couchdb-scala) - Purely functional Scala client for CouchDB
* **[doobie ★ 812 ⧗ 0](https://github.com/tpolecat/doobie)** - Pure functional JDBC layer for Scala.
* **[Elastic4s ★ 1049 ⧗ 0](https://github.com/sksamuel/elastic4s)** - A scala DSL / reactive client for Elasticsearch
* [Finagle ★ 42 ⧗ 71](https://github.com/finagle/finagle-postgres) - PostgreSQL protocol support for Finagle
* [longevity ★ 78 ⧗ 21](https://github.com/longevityframework/longevity) - A Persistence Framework for Scala and NoSQL with a Domain Driven Design Orientation
* [lucene4s ★ 3 ⧗ 56](https://github.com/outr/lucene4s) - Light-weight convenience wrapper around Lucene to simplify complex tasks and add Scala sugar.
* [MapperDao ★ 12 ⧗ 36](https://github.com/kostaskougios/mapperdao) - An ORM library for oracle, mysql, mssql, and postgresql
* [Memcontinuationed ★ 51 ⧗ 245](https://github.com/Atry/memcontinuationed) - Memcached client for Scala.
* [Morpheus ★ 104 ⧗ 0](https://github.com/outworkers/morpheus) - Reactive type safe Scala Driver for MySQL/Postgres.
* [neo4akka ★ 6 ⧗ 117](https://github.com/outr/neo4akka) - Neo4j Scala client using Akka HTTP with compile-time query interpolation, case class support, true non-blocking IO, and much more.
* [neotypes ★ 22 ⧗ 2](https://github.com/neotypes/neotypes) - Pure functional driver for neo4j.
* **[Phantom ★ 903 ⧗ 5](https://github.com/outworkers/phantom)** - Reactive typed Scala driver for Apache Cassandra.
* **[PostgreSQL and MySQL async ★ 983 ⧗ 0](https://github.com/mauricio/postgresql-async)** - Async database drivers to talk to PostgreSQL and MySQL in Scala.
* [Pulsar4s ★ 15](https://github.com/sksamuel/pulsar4s) - Scala client for Apache Pulsar.
* **[Quill ★ 865 ⧗ 0](https://github.com/getquill/quill)** - Compile-time Language Integrated Query for Scala
* [ReactiveCouchbase](http://reactivecouchbase.org/) - Reactive Scala Driver for Couchbase. Also includes a Play plug-in. An official plug-in is also in development.
* **[ReactiveMongo ★ 704 ⧗ 8](https://github.com/ReactiveMongo/ReactiveMongo)** - Reactive Scala Driver for MongoDB.
* **[rediscala ★ 642 ⧗ 0](https://github.com/etaty/rediscala)** - Non-blocking, Reactive Redis driver for Scala (with Sentinel support)
* [Relate ★ 110 ⧗ 7](https://github.com/lucidsoftware/relate) - Lightweight, blazing-fast database access layer for Scala that abstracts the idiosyncricies of the JDBC while keeping complete control over the SQL.
* [Salat ★ 490 ⧗ 9](https://github.com/salat/salat/) - ORM for MongoDB. A related Play-plugin is also available.
* [Scala ActiveRecord ★ 297 ⧗ 3](https://github.com/aselab/scala-activerecord) - ORM library for scala, inspired by ActiveRecord of Ruby on Rails.
* [Scala-Forklift ★ 91 ⧗ 1](https://github.com/lastland/scala-forklift) - Type-safe database migration for Slick, Git, etc.
* **[scala-redis ★ 739 ⧗ 1](https://github.com/debasishg/scala-redis)** - A Scala library for connecting to a redis server, with clustering support
* [scala-sql ★ 14 ⧗ 34](https://github.com/wangzaixiang/scala-sql) - Yet another SQL-based DB access library for scala language
* [ScalaRelational ★ 51 ⧗ 1](https://github.com/outr/scalarelational) - Type-Safe framework for defining, modifying, and querying SQL databases.
* **[ScalikeJDBC ★ 746 ⧗ 1](https://github.com/scalikejdbc/scalikejdbc)** - A tidy SQL-based DB access library for Scala developers.
* [Scanamo ★ 92 ⧗ 1](https://github.com/guardian/scanamo) - A library to make using DynamoDB with Scala simpler and less error-prone.
* [scredis ★ 149 ⧗ 29](https://github.com/Livestream/scredis) - Non-blocking Redis client built on top of Akka IO (used by Livestream)
* [Shade ★ 82 ⧗ 32](https://github.com/alexandru/shade) - Memcached client for Scala, based on Spymemcached
* **[Slick ★ 1795 ⧗ 0](https://github.com/slick/slick)** - Modern database query and access library for Scala.
* [Slick-pg ★ 714](https://github.com/tminglei/slick-pg) - Slick extensions for PostgreSQL.
* [Sorm ★ 239 ⧗ 2](https://github.com/sorm/sorm) - A functional boilerplate-free Scala ORM.
* [Squeryl ★ 484 ⧗ 1](https://github.com/squeryl/squeryl) - A Scala DSL for talking with databases with minimum verbosity and maximum type safety.
* [Sangria](https://sangria-graphql.org/) - Scala GraphQL Implementation
* [Scruid ★ 48](https://github.com/ing-bank/scruid) - Scruid (Scala+Druid) is an open source library that allows you to compose Druid queries easily in Scala.
* [Tepkin ★ 86 ⧗ 251](https://github.com/fehmicansaglam/tepkin) - Reactive MongoDB Driver for Scala built on top of Akka IO and Akka Streams.

## Messaging

* [Op-Rabbit ★ 153 ⧗ 2](https://github.com/SpinGo/op-rabbit) - High-level messaging library for Akka and Op-Rabbit.

## Graphical User Interfaces

*Libraries for creation of graphical user interfaces*

* [ScalaFX](http://www.scalafx.org/) - Scala DSL for creating Graphical User Interfaces that sits on top of JavaFX.

## Web Frameworks

*Scala frameworks for web development.*

* [Analogweb](https://github.com/analogweb/analogweb-scala) - Tiny, simple, and pluggable web framework in Scala.
* [Chaos ★ 220 ⧗ 27](https://github.com/mesosphere/chaos) - A lightweight framework for writing REST services in Scala.
* **[Colossus ★ 811 ⧗ 70](http://tumblr.github.io/colossus/)** - lightweight framework for building high-performance applications in Scala that require non-blocking network I/O.
* **[Finatra ★ 1558 ⧗ 0](https://github.com/twitter/finatra)** - A sinatra-inspired web framework for scala, running on top of Finagle.
* **[Lift ★ 1069 ⧗ 0](https://github.com/lift/framework)** - Secure and powerful full stack web framework ([discussion](https://github.com/lauris/awesome-scala/pull/19)).
* [peregine ★ 11 ⧗ 40](https://github.com/dvarelap/peregrine) - A simple and async lightweight Scala web framework.
* **[Play ★ 9229 ⧗ 0](https://github.com/playframework/playframework)** - Makes it easy to build scalable, fast and real-time web applications with Java & Scala.
* [Play Pagelets ★ 47 ⧗ 11](https://github.com/splink/pagelets) - A Module for the Play Framework to build resilient and modular Play applications in an elegant and concise manner.
* [Reactive ★ 194 ⧗ 6](https://github.com/nafg/reactive) - FRP and web abstractions, which can be plugged into any web framework (currently only has bindings for Lift).
* **[scalajs-react ★ 1135 ⧗ 0](https://github.com/japgolly/scalajs-react)** - Facebook's React on Scala.JS.
* **[Scalatra ★ 2146 ⧗ 0](https://github.com/scalatra/scalatra)** - Tiny Scala high-performance, async web framework, inspired by Sinatra.
* **[Skinny Framework ★ 621 ⧗ 1](https://github.com/skinny-framework/skinny-framework)** - A full-stack web app framework upon Scalatra for rapid Development in Scala.
* [suzaku](https://github.com/suzaku-io/suzaku) - Suzaku web UI framework for Scala
* **[Unfiltered ★ 673 ⧗ 6](https://github.com/unfiltered/unfiltered)** - A modular set of unopinionated primitives for servicing HTTP and WebSocket requests in Scala.
* [Xitrum](http://xitrum-framework.github.io/) - An async and clustered Scala web framework and HTTP(S) server fusion on top of Netty, Akka, and Hazelcast.
* [youi ★ 81 ⧗ 12](https://github.com/outr/youi) - Next generation user interface framework and server engine for Scala and Scala.js.

## Reactive Web Frameworks

*Scala libraries for Reactive Web development*

* **[Binding.scala ★ 935 ⧗ 0](https://github.com/ThoughtWorksInc/Binding.scala)** - A reactive web framework. It enables you use native XML literal syntax to create reactive DOM nodes, which are able to automatically change whenever the data source changes.
* [Korolev](http://github.com/fomkin/korolev/) - Modern single-page applications running on the server side
* [Udash](http://udash.io/) - a web framework based on Scala.js with support for property bindings, frontend routing, i18n and much more. It also provides strongly typed client<->server RPC system based on WebSockets.
* [Vert.x Web](http://vertx.io/docs/vertx-web/scala/) - Toolkit to build Reactive web applications..
* [Widok](https://widok.github.io/) - Reactive web framework for the JVM and Scala.js

## Data Binding and Validation

*Scala libraries for data binding and validation*

* [Accord ★ 379 ⧗ 0](https://github.com/wix/accord) - A sane validation library for Scala
* [form-binder ★ 17 ⧗ 29](https://github.com/tminglei/form-binder) - A micro data binding and validating framework, very easy to use and hack
* [Monkeytail ★ 55](https://github.com/sksamuel/monkeytail) - A set of validation macros and helpers for cats.Validated
* [Octopus ★ 15](https://github.com/krzemin/octopus) - Scala library for boilerplate-free validation

## i18n

*Scala libraries for i18n.*

* [scala-xgettext ★ 19 ⧗ 99](https://github.com/xitrum-framework/scala-xgettext) - A compiler plugin that acts like GNU xgettext command to extract i18n strings in Scala source code files to Gettext .po file.
* [Scaposer ★ 30 ⧗ 99](https://github.com/xitrum-framework/scaposer) - GNU Gettext .po file loader for Scala.

## Authentication

*Libraries for implementing authentications schemes.*

* [akka-http-session ★ 268 ⧗ 11](https://github.com/softwaremill/akka-http-session) - Web&mobile client-side sessions for akka-http based applications, with optional JWT support
* [AWS Request Signer ★ 4 ⧗ 43](https://github.com/ticofab/aws-request-signer) - Helper to evaluate the signing headers for HTTP requests to Amazon Web Services.
* [OAuth2-mock-play ★ 16 ⧗ 23](https://github.com/zalando/OAuth2-mock-play) - Implementation of an OAuth2 server designed for mocking/testing and configurable by environment variables (by use of the Typesafe config).
* [Play Google Auth Module ★ 17 ⧗ 76](https://github.com/guardian/play-googleauth) - A very simple implementation of Google OpenID Connect authentication for Play 2 applications.
* [play-pac4j ★ 255 ⧗ 0](https://github.com/pac4j/play-pac4j) - Security library managing authentication (CAS, OAuth, OpenID, SAML, LDAP, SQL, JWT...), authorizations and logout for Play 2.x in Java and Scala.
* **[play-silhouette ★ 600 ⧗ 1](https://github.com/mohiva/play-silhouette)** - Authentication library for Play Framework applications that supports several authentication methods, including OAuth1, OAuth2, OpenID, Credentials or custom authentication schemes.
* **[play2-auth ★ 617 ⧗ 4](https://github.com/t2v/play2-auth)** - Play2.x Authentication and Authorization module.
* [scala-oauth2-provider ★ 419 ⧗ 7](https://github.com/nulab/scala-oauth2-provider) - OAuth 2.0 server-side implementation written in Scala.
* **[SecureSocial ★ 1210 ⧗ 1](https://github.com/jaliss/securesocial)** - A module that provides OAuth, OAuth2 and OpenID authentication for Play Framework applications.

## Authorization

*Libraries for implementing authorization strategies.*

* [deadbolt-2 ★ 467 ⧗ 3](https://github.com/schaloner/deadbolt-2) - A Play 2.x module supporting role-based and proprietary authorization; idiomatic APIs for Scala and Java APIs are provided.

## Cryptography

*Cryptography and Encryption Libraries.*

* [Scrypto ★ 50 ⧗ 4](https://github.com/ScorexProject/scrypto) - All-purpose cryptographic framework.
* [TSec ★ 27 ⧗ 0](https://github.com/jmcardon/tsec) - Type-safe, functional, general-cryptography library

## Testing

*Libraries for code testing.*

* [cornichon ★ 109 ⧗ 3](https://github.com/agourlay/cornichon) - Scala DSL for testing HTTP JSON API.
* [Gatling](http://gatling.io) - Async Scala-Akka-Netty based Stress Tool.
* [Minitest](https://github.com/monix/minitest) - A testing framework with a focus on simplicity.
* [Mockito Scala ★ 99](https://github.com/mockito/mockito-scala) - Mockito for Scala, with improved syntax and many extra features on top of the Java version
* **[ScalaCheck ★ 1196 ⧗ 6](https://github.com/rickynils/scalacheck)** - Property-based testing for Scala.
* [ScalaMeter](https://scalameter.github.io/) - Performance &  memory footprint measuring, regression testing.
* [ScalaMock](http://scalamock.org) - Scala native mocking framework
* [scalaprops ★ 171 ⧗ 5](https://github.com/scalaprops/scalaprops) - Another property based testing library for Scala
* **[ScalaTest ★ 532 ⧗ 5](https://github.com/scalatest/scalatest)** - A testing tool for Scala and Java developers.
* [Scalive ★ 187 ⧗ 20](https://github.com/xitrum-framework/scalive) - Connect a Scala REPL to running JVM processes without any prior setup; this library is used for inspecting systems in production mode.
* **[Specs2 ★ 570 ⧗ 1](https://github.com/etorreborre/specs2)** - Software Specifications for Scala.
* [Stryker4s ★ 21](https://github.com/stryker-mutator/stryker4s) - Test your tests with mutation testing.
* [µTest ★ 197 ⧗ 0](https://github.com/lihaoyi/utest) - A tiny, portable testing library for Scala.
* [testcontainers-scala ★ 52 ⧗ 2](https://github.com/testcontainers/testcontainers-scala) - Docker containers for testing in Scala.

## JSON

*Libraries for work with json.*

* [argonaut](http://argonaut.io/) - Purely Functional JSON in Scala.
* **[circe ★ 824 ⧗ 2](https://github.com/travisbrown/circe)** - JSON library based on Argonaut, depends on Cats
* [diffson ★ 94 ⧗ 14](https://github.com/gnieh/diffson) - A scala diff/patch library for Json
* [jackson-module-scala ★ 313 ⧗ 8](https://github.com/FasterXML/jackson-module-scala) - Add-on module for Jackson to support Scala-specific datatypes.
* [jawn ★ 252 ⧗ 4](https://github.com/non/jawn) - Fast json parser (According to them, competetive with java gson/jackson speed).
* **[json4s ★ 877 ⧗ 0](https://github.com/json4s/json4s)** - Project aims to provide a single AST to be used by other scala json libraries.
* [jsoniter-scala ★ 47 ⧗ 7](https://github.com/plokhotnyuk/jsoniter-scala) - Scala macros for compile-time generation of ultra-fast JSON codecs.
* [persist-json ★ 9 ⧗ 49](https://github.com/nestorpersist/json) - Fast json parser.
* [play-json ★ 39 ⧗ 7](https://github.com/playframework/play-json) - Flexible and powerful JSON manipulation, validation and serialization, with no reflection at runtime.
* [Pushka ★ 75 ⧗ 21](https://github.com/fomkin/pushka) - Scala JSON serialization library with annotations.
* [qbproject](https://github.com/qb-project/qbproject) - Scala Libs around JSON and API development for Play Framework.
* [rapture-json](https://github.com/propensive/rapture/blob/dev/doc/json.md) - Clean, intuitive, unintrusive, boilerplate-free Scala API
* [scala-jsonapi ★ 95 ⧗ 240](https://github.com/scala-jsonapi/scala-jsonapi) - Support library for integrating the JSON API spec with Scala and Spray JSON, Play! JSON or Circe.
* [scalajack ★ 81 ⧗ 35](https://github.com/gzoller/ScalaJack) - Fast 'n easy JSON serialization with optional MongoDB support.  Uses Jackson under the hood.
* **[spray-json ★ 606 ⧗ 2](https://github.com/spray/spray-json)** - Lightweight, clean and efficient JSON implementation in Scala.
* [sbt-json](https://github.com/battermann/sbt-json) - sbt plugin that generates Scala case classes for easy, statically typed and implicit access of JSON documents
* [uJson](http://www.lihaoyi.com/upickle/#uJson) - fast, flexible and intuitive JSON for Scala

## YAML

*Libraries for work with YAML.*

* [MoultingYAML ★ 43 ⧗ 2](https://github.com/jcazevedo/moultingyaml) - Type-class based YAML serialization and deserialization on top of SnakeYAML.

## CSV

*Libraries for work with CSV.*

* [fm-flatfile ★ 1 ⧗ 1](https://github.com/frugalmechanic/fm-flatfile) - Very flexible, Flat File (CSV, TSV, Excel, etc) Reader for Scala.
* [kantan.csv ★ 143 ⧗ 24](https://github.com/nrinaudo/kantan.csv) - CSV handling library for Scala with multiple backends.
* [Scala-CSV ★ 365 ⧗ 1](https://github.com/tototoshi/scala-csv) - CSV Reader/Writer for Scala.


## Serialization

*Libraries for serializing and deserializing data for storage or transport.*

* [avro-codegen ★ 24 ⧗ 23](https://github.com/Nitro/avro-codegen) - Code generation from avro schemas to serialize/deserialize avro messages, no runtime reflection.
* [Avro4s ★ 473](https://github.com/sksamuel/avro4s) - Avro schema generation and serialization / deserialization for Scala.
* [Chill ★ 378 ⧗ 4](https://github.com/twitter/chill) - Extensions for the Kryo serialization library to ease configuration in systems like Hadoop and Storm.
* [msgpack ★ 75 ⧗ 57](https://github.com/msgpack/msgpack-scala) - A efficient binary serialization library.
* **[Pickling ★ 808 ⧗ 0](https://github.com/scala/pickling)** - Fast, customizable, boilerplate-free pickling support.
* [µPickle](http://lihaoyi.github.io/upickle/) - A lightweight serialization library for Scala that works in ScalaJS, allowing transfer of structured data between the JVM and JavaScript.
* [ScalaBuff ★ 218 ⧗ 1](https://github.com/SandroGrzicic/ScalaBuff) - a Scala Protocol Buffers (protobuf) compiler
* **[ScalaPB ★ 705 ⧗ 51](https://scalapb.github.io/)** - Protocol Buffers and gRPC support for Scala
* [scodec ★ 474 ⧗ 10](https://github.com/scodec/scodec) - A combinator library for working with binary data.
* [Scrooge](http://twitter.github.io/scrooge/) - An Apache Thrift code generator for Scala.
* [validation ★ 177 ⧗ 3](https://github.com/jto/validation) - Advanced validation & serialization for JSON, HTML form data, etc, with no reflection at runtime.

## Science and Data Analysis

*Libraries for scientific computing, data analysis and numerical processing.*

* **[Algebird ★ 1478 ⧗ 0](https://github.com/twitter/algebird)** - Abstract Algebra for Scala.
* [Axle ★ 51 ⧗ 9](https://github.com/axlelang/axle) - A Spire-based DSL for scientific cloud computing.
* **[BigDL ★ 1662 ⧗ 0](https://github.com/intel-analytics/BigDL)** - BigDL is a distributed deep learning library for Apache Spark.
* **[Breeze ★ 2028 ⧗ 0](https://github.com/scalanlp/breeze)** - Breeze is a numerical processing library for Scala.
* [Chalk ★ 231 ⧗ 6](https://github.com/scalanlp/chalk) - Chalk is a natural language processing library.
* [Clustering4Ever ★ 50](https://github.com/Clustering4Ever/Clustering4Ever) Scala and Spark API to benchmark and analyse clustering algorithms on any vectorization you can generate
* [doddle-model](https://github.com/picnicml/doddle-model) - An in-memory machine learning library built on top of Breeze. It provides immutable objects and exposes its functionality through a scikit-learn-like API.
* [FACTORIE ★ 486 ⧗ 7](https://github.com/factorie/factorie) - A toolkit for deployable probabilistic modeling, implemented as a software library in Scala.
* [Figaro ★ 461 ⧗ 0](https://github.com/p2t2/figaro) - Figaro is a probabilistic programming language that supports development of very rich probabilistic models.
* [Libra ★ 142](https://github.com/to-ithaca/libra) - Libra is a dimensional analysis library based on shapeless, spire and singleton-ops. It contains out of the box support for SI units for all numeric types.
* [LoMRF ★ 55](https://github.com/anskarl/LoMRF) - An open-source implementation of Markov Logic Networks in Scala
* [MGO ★ 37 ⧗ 55](https://github.com/openmole/mgo) - Modular multi-objective evolutionary algorithm optimization library enforcing immutability.
* [MLLib](https://spark.apache.org/mllib/) - Machine Learning framework for Spark
* [ND4S ★ 201 ⧗ 0](https://github.com/deeplearning4j/nd4s) - N-Dimensional arrays and linear algebra for Scala with an API similar to Numpy.  ND4S is a scala wrapper around [ND4J](http://nd4j.org/).
* [Numsca ★ 8 ⧗ 0](https://github.com/botkop/numsca) - Numsca is Numpy for Scala.
* [OpenMOLE ★ 65 ⧗ 5](https://github.com/openmole/openmole) - OpenMOLE (Open MOdeL Experiment) is a workflow engine designed to leverage the computing power of distributed execution environments for naturally parallel processes.
* [Optimus * 96](https://github.com/vagmcs/Optimus) Optimus is a library for Linear and Quadratic mathematical optimization written in Scala programming language.
* [OscaR](https://bitbucket.org/oscarlib/oscar/wiki/Home) - a Scala toolkit for solving Operations Research problems
* [Persist-Units ★ 9 ⧗ 40](https://github.com/nestorpersist/units) - Type check units of measure in Scala.
* **[PredictionIO ★ 10105 ⧗ 0](https://github.com/PredictionIO/PredictionIO)** - machine learning server for developers and data scientists. Built on Apache Spark, HBase and Spray
* [Rings ★ 3 ⧗ 0](https://github.com/PoslavskySV/rings) - An efficient library for polynomial rings. Commutative algebra, polynomial GCDs, polynomial factorization and other sci things at a really high speed.
* [Saddle ★ 428 ⧗ 2](https://github.com/saddle/saddle) - A minimalist port of Pandas to Scala
* [Smile](http://haifengl.github.io/smile/) - Statistical Machine Intelligence and Learning Engine. Smile is a fast and comprehensive machine learning system.
* **[Spark Notebook ★ 1896 ⧗ 0](https://github.com/andypetrella/spark-notebook)** - Scalable and stable Scala and Spark focused notebook bridging the gap between JVM and Data Scientists (incl. extendable, typesafe and reactive charts).
* **[Spire ★ 1152 ⧗ 3](https://github.com/non/spire)** - Powerful new number types and numeric abstractions for Scala.
* [Squants ★ 388 ⧗ 1](https://github.com/garyKeorkunian/squants) - The Scala API for Quantities, Units of Measure and Dimensional Analysis.
* [SwiftLearner ★ 20 ⧗ 5](https://github.com/valdanylchuk/swiftlearner) - Simply written algorithms to help study Machine Learning or write your own implementations.
* [Tensorflow_scala](https://github.com/eaplatanios/tensorflow_scala) - TensorFlow API for the Scala Programming Language
* [Tyche ★ 89 ⧗ 17](https://github.com/neysofu/tyche) - Probability distributions, stochastic & Markov processes, lattice walks, simple random sampling. A simple yet robust Scala library.
* [Zeppelin](http://zeppelin-project.org/) - Scala and Spark Notebook (like IPython Notebook)


## Big Data

* **[BIDMach ★ 745 ⧗ 0](https://github.com/BIDData/BIDMach)** - CPU and GPU machine learning library, using JNI for GPU computation.
* **[Flink ★ 2414 ⧗ 0](https://github.com/apache/flink)** - Processing framework with powerful stream- and batch-processing capabilities.
* **[Gearpump ★ 619 ⧗ 5](https://github.com/apache/incubator-gearpump)** - Lightweight real-time big data streaming engine
* [GridScale ★ 15 ⧗ 5](https://github.com/openmole/gridscale) - A Scala API for computing clusters and grids.
* **[Kafka ★ 5035 ⧗ 0](https://github.com/apache/kafka)** - Kafka is a message broker project and aims to provide a unified, high-throughput, low-latency platform for handling real-time data feeds.
* **[Reactive-kafka ★ 753 ⧗ 0](https://github.com/akka/reactive-kafka)** - Reactive Streams API for Apache Kafka.
* **[Scalding ★ 2783 ⧗ 2](https://github.com/twitter/scalding)** - A Scala binding for the Cascading abstraction of Hadoop MapReduce.
* [Schemer](https://github.com/indix/schemer) - Schema registry for CSV, TSV, JSON, AVRO and Parquet schema. Supports schema inference and GraphQL API.
* [Scio](https://github.com/spotify/scio) - A Scala API for [Apache Beam](https://beam.apache.org/) and [Google Cloud Dataflow](https://cloud.google.com/dataflow/) - None
* [Scrunch](http://crunch.apache.org/scrunch.html) - A Scala wrapper for [Apache Crunch](http://crunch.apache.org/index.html) which provides a framework for writing, testing, and running MapReduce pipelines.
* [Spark](http://spark.apache.org/) - Lightning fast cluster computing — up to 100x faster than Hadoop for iterative algorithms (memory caching) and up to 10x faster than Hadoop for single-pass MapReduce jobs. Compatible with YARN-enabled Hadoop clusters, can run on Mesos and in stand-alone mode as well.
* [spark-deployer ★ 69 ⧗ 29](https://github.com/KKBOX/spark-deployer) - A sbt plugin which helps deploying Apache Spark stand-alone cluster and submitting job on cloud system like AWS EC2.
* [Sparkta ★ 320 ⧗ 1](https://github.com/Stratio/sparkta) - Real Time Aggregation based on Spark Streaming.
* [Sparkplug ★ 4 ⧗ 1](https://github.com/indix/sparkplug) - Spark package to "plug" holes in data using SQL based rules
* **[Summingbird ★ 1841 ⧗ 1](https://github.com/twitter/summingbird)** - An implementation of the “lambda architecture” as a software abstraction — a single API for Hadoop and Storm.
* [Vegas](https://github.com/vegas-viz/Vegas) - The missing MatPlotLib for Scala + Spark

## Image processing and image analysis

*2D and 3D image processing and image analysis*

* [scala-phash ★ 11 ⧗ 2](https://github.com/poslegm/scala-phash) - Image comparison by hash codes
* [scalismo ★ 45 ⧗ 9](https://github.com/unibas-gravis/scalismo) - Shape modelling and  model-based image analysis.
* **[scrimage ★ 654 ⧗ 97](https://github.com/sksamuel/scrimage)** - Image io, resize, manipulation and thumbnails.

## Sound processing and music

* [Chromaprint.scala ★ 31](https://github.com/mgdigital/Chromaprint.scala) - A Scala implementation of the Chromaprint/AcoustID audio fingerprinting algorithm.
* [ScalaCollider ★ 121 ⧗ 5](https://github.com/Sciss/ScalaCollider) - Sound synthesis and signal processing client for SuperCollider.

## Functional Reactive Programming

*Event streams, signals, observables, etc.*

* **[fs2 ★ 1323 ⧗ 340](https://github.com/functional-streams-for-scala/fs2)** - Compositional, streaming I/O library for Scala
* [Iteratee ★ 158](https://github.com/travisbrown/iteratee) - Iteratees for cats
* **[Monix ★ 1432 ⧗ 164](https://github.com/monix/monix)** - Extensions to Scala’s standard library for multi-threading primitives and functional reactive programming. Scala.js compatible.
* [Reactive Collections ★ 2 ⧗ 165](https://github.com/storm-enroute/reactors) - A library that incorporates event streams and signals with specialized collections called reactive containers, and expresses concurrency using isolates and channels.
* **[RxScala ★ 824 ⧗ 0](https:65]529//github.com/ReactiveX/RxScala)** - Reactive Extensions for Scala – a library for composing asynchronous and event-based programs using observable sequences
* [REScala](http://www.rescala-lang.com/) - REScala is a library for functional reactive programming on the JVM and the Web. It provides a rich API for event stream transformations and signal composition with managed consistent up-to-date state and minimal syntactic overhead.
* [Reactor-Scala-Extensions](https://github.com/reactor/reactor-scala-extensions) - Scala extensions for [Project Reactor](http://projectreactor.io)
* [scala.frp ★ 22 ⧗ 101](https://github.com/dylemma/scala.frp) - Functional Reactive Programming for Scala (event streams).
* **[Scala.Rx ★ 898 ⧗ 4](https://github.com/lihaoyi/scala.rx)** - An experimental library for Functional Reactive Programming in Scala (reactive variables). Scala.js compatible.
* [Scalaz ZIO ★ 529](https://github.com/scalaz/scalaz-zio) - A type-safe, composable library for asynchronous and concurrent programming in Scala
* [SynapseGrid ★ 109 ⧗ 1](https://github.com/Primetalk/SynapseGrid) - an FRP framework for constructing reactive real-time immutable data flow systems. It implements an original way of running and organizing event-driven systems based on Petri nets. The topology can be viewed as a .dot graph. The library is compatible with Akka and can seamlessly communicate with other actors.
* [Vert.x](http://vertx.io/) - A polyglot reactive application platform for the JVM which aims to be an alternative to node.js. Its concurrency model resembles actors. It supports [Scala](http://vertx.io/docs/vertx-core/scala/), Clojure, Java, Javascript, Ruby, Groovy and Python.

## Modularization and Dependency Injection

*Modularization of applications, dependency injection, etc.*

* [Airframe ★ 25 ⧗ 13](https://github.com/wvlet/airframe) - Dependency injection library tailored to Scala.
* [Cableguy ★ 1 ⧗ 269](https://github.com/akozhemiakin/cableguy) - Macro based compile time Dependency Injection library.
* [DIStage ★ 75 ⧗ 0](https://github.com/7mind/izumi) - Staged Dependency Injection with higher-kinded polymorphism and cats/zio support.
* [Grafter ★ 148 ⧗ 0](https://github.com/zalando/grafter) - Grafter is a library to configure and wire Scala applications.
* **[MacWire ★ 661 ⧗ 0](https://github.com/adamw/macwire)** - Scala Macro to generate wiring code for class instantiation. DI container replacement.
* [Scala-Guice ★ 211 ⧗ 10](https://github.com/codingwell/scala-guice) - Scala extensions for Google Guice
* [Scaldi ★ 252 ⧗ 1](https://github.com/scaldi/scaldi) - Lightweight Scala Dependency Injection Library.
* [Sclasner ★ 9 ⧗ 130](https://github.com/xitrum-framework/sclasner) - Scala classpath scanner.
* [SubCut ★ 403 ⧗ 9](https://github.com/dickwall/subcut) - Scala Uniquely Bound Classes Under Traits.

## Distributed Systems

*Libraries and frameworks for writing distributed applications.*

* [Akka](http://akka.io/) - A toolkit and runtime for building highly concurrent, distributed, and fault tolerant event-driven applications.
* [Akka-tracing ★ 252 ⧗ 2](https://github.com/levkhomich/akka-tracing) - A distributed tracing extension for Akka. Provides integration with Play framework, Spray and Akka HTTP.
* [autobreaker ★ 6 ⧗ 93](https://github.com/lucastorri/autobreaker) - Automatically wrap classes that return Futures with a [Circuit Breaker](http://martinfowler.com/bliki/CircuitBreaker.html).
* [Clump](http://getclump.io) - A library for expressive and efficient service composition
* [CurioDB ★ 459 ⧗ 4](https://github.com/stephenmcd/curiodb) - Distributed & Persistent Redis Clone built with Scala & Akka.
* [Finagle](https://twitter.github.io/finagle/) - An extensible, protocol-agnostic RPC system designed for high performance and concurrency.
* [Glokka ★ 46 ⧗ 148](https://github.com/xitrum-framework/glokka) - Library to register and lookup actors by names in an Akka cluster.
* [Lagom](https://www.lightbend.com/lagom) - Framework for creating microservice-based systems.
* [Reactors](http://reactors.io/) - Foundational framework for distributed computing that fuses functional reactive programming and traditional actors.
* [Parapet](https://github.com/parapet-io/parapet) - A purely functional library to build distributed and event-driven systems

## Extensions

*Scala extensions.*

* [Ammonite-Ops](http://lihaoyi.github.io/Ammonite/#Ammonite-Ops) - Safe, easy, filesystem operations in Scala as convenient as in the Bash shell.
* **[better-files ★ 824 ⧗ 0](https://github.com/pathikrit/better-files)** - Simple, safe and intuitive Scala I/O. better-files is a dependency-free pragmatic thin Scala wrapper around Java NIO.
* **[Cassovary ★ 881 ⧗ 0](https://github.com/twitter/cassovary)** - A Scala library that is designed from the ground up for space efficiency, handling graphs with billions of nodes and edges.
* **[cats ★ 1697 ⧗ 0](https://github.com/typelevel/cats)** - Lightweight, modular, and extensible library for functional programming.
* [Chimney ★ 92 ⧗ 5](https://github.com/scalalandio/chimney) - Scala library for boilerplate-free data transformations.
* [chronoscala ★ 38 ⧗ 0](https://github.com/opt-tech/chronoscala) - Scala wrapper for Java Date/Time API.
* [Dsl.scala](https://github.com/ThoughtWorksInc/Dsl.scala/) - A framework to create embedded Domain-Specific Languages in Scala, along with some built-in DSLs, including async/await, generators, delimited continuations, asynchronous collection comprehension, RAII, monadic !-notation for cats and scala, etc.
* [Each ★ 146 ⧗ 0](https://github.com/ThoughtWorksInc/each) - A macro library that converts native imperative syntax to [Scalaz](https://github.com/scalaz/scalaz)'s monadic expressions.
* [Eff ★ 220 ⧗ 6](https://github.com/atnos-org/eff) - Extensible effects are an alternative to monad transformers for computing with effects in a functional way.
* [enableIf.scala ★ 40 ⧗ 25](https://github.com/ThoughtWorksInc/enableIf.scala) - A library that switches Scala code at compile-time, like `#if` in C/C++.
* [Enumeratum ★ 374 ⧗ 0](https://github.com/lloydmeta/enumeratum) - A macro to replace Scala enumerations with a sealed family of case objects. This allows additional checks for the compiler, e.g. for missing cases in a match statement. Has additinal support for Json libraries and the Play framework.
* [Freasy-Monad ★ 90 ⧗ 14](https://github.com/Thangiee/Freasy-Monad) - Easy way to create Free Monad for Cats and Scalaz using Scala macros with first-class Intellij support.
* [Freedsl ★ 25 ⧗ 5](https://github.com/ISCPIF/freedsl) - A library to implement composable side effects, weaving typeclasses on a wrapping type and the free monad.
* [Freestyle ★ 430 ⧗ 0](https://github.com/frees-io/freestyle) - A cohesive & pragmatic framework of FP centric Scala libraries.
* [Hamsters ★ 216 ⧗ 0](https://github.com/scala-hamsters/hamsters) - A mini Scala utility library. Compatible with functional programming beginners. Featuring validation, monad transformers, HLists, Union types.
* [idid ★ 4 ⧗ 43](https://github.com/lucastorri/idid) - A library to define common interfaces for different Id types.
* [Lamma ★ 70 ⧗ 8](https://github.com/maxcellent/lamma) - A Scala date library for date and schedule generation.
* [LArray ★ 225 ⧗ 25](https://github.com/xerial/larray) - Large off-heap arrays (> 2GB) and mmap files.
* [Log4s](http://www.log4s.org/) - Fast, Scala-friendly logging bindings on top of [SLF4J](http://slf4j.org/). Uses macros for extreme performance.
* [LogStage ★ 75 ⧗ 0](https://github.com/7mind/izumi) - Zero-effort structural logger for Scala with [SLF4J] integration.
* **[Scala-Logging ★ 707](https://github.com/lightbend/Scala-Logging)** - Convenient and performant logging library for Scala wrapping SLF4J.
* **[Monocle ★ 757 ⧗ 0](https://github.com/julien-truffaut/Monocle)** - An Optics/Lens library for purely functional manipulation of immutable objects.
* **[n-scala ★ 662 ⧗ 3](https://github.com/nscala-time/nscala-time)** - Scala wrapper for Joda Time.
* [Persist-Logging ★ 33 ⧗ 48](https://github.com/nestorpersist/logging) - Comprehensive logging library for Scala.
* [Quicklens ★ 245 ⧗ 0](https://github.com/adamw/quicklens) - modify deeply nested case class fields with an elegant API
* [Rapture](http://rapture.io/) ([repo](https://github.com/propensive/rapture)) - a collection of libraries for common, everyday programming tasks (I/O, JSON, i18n, etc.)
* [Records for Scala ★ 125 ⧗ 55](https://github.com/scala-records/scala-records) - Labeled records for Scala based on structural refinement types and macros.
* [refined ★ 447 ⧗ 3](https://github.com/fthomas/refined) - Simple refinement types with compile- and runtime checking
* [Resolvable ★ 0 ⧗ 94](https://github.com/stanch/resolvable) - A library to optimize fetching immutable data structures from several endpoints in several formats.
* [Squid ★ 88 ⧗ 9](https://github.com/epfldata/squid) - Type-safe metaprogramming framework with typed, hygienic quasiquotes.
* **[Scala Async ★ 778 ⧗ 0](https://github.com/scala/async)** - An asynchronous programming facility for Scala.
* [Scala Graph](http://www.scala-graph.org/) - A Scala library with basic graph functionality that seamlessly fits into the Scala standard collections library.
* [scala.meta](http://scalameta.org/) - A clean-room implementation of a metaprogramming toolkit for Scala.
* [Scalactic](http://www.scalactic.org/) - Small library of utilities related to quality that helps keeping code clear and correct.
* **[Scalaz ★ 3045 ⧗ 0](https://github.com/scalaz/scalaz)** - An extension to the core Scala library for functional programming.
* [scribe ★ 36 ⧗ 3](https://github.com/outr/scribe) - Practical logging framework that doesn't depend on any other logging framework and can be completely configured programmatically.
* **[Shapeless ★ 2002 ⧗ 0](https://github.com/milessabin/shapeless)** - A type class and dependent type based generic programming library for Scala.
* [Simulacrum ★ 484 ⧗ 2](https://github.com/mpilquist/simulacrum) - First class syntax support for type classes in Scala.
* [Stateless Future ★ 165 ⧗ 35](https://github.com/qifun/stateless-future) - Asynchronous programming in fully featured Scala syntax.
* [tinylog ★ 198 ⧗ 0](https://github.com/pmwmedia/tinylog) - Lightweight logging framework with native logging API for Scala.
* **[Twitter Util ★ 1809 ⧗ 1](https://github.com/twitter/util)** - General-purpose Scala libraries, including a future implementation and other concurrency tools.
* [wvlet-log ★ 43 ⧗ 13](https://github.com/wvlet/log) - A library for enhancing your application logs with colors and source code locations.

## Misc

*Projects that don't fit into any specific category.*

* [Agora](https://gitlab.com/aossie/Agora/) - Library of vote-counting algorithms for elections.
* [Ammonite-REPL](http://lihaoyi.github.io/Ammonite/#Ammonite-REPL) - An improved Scala REPL: syntax highlighting, output formatting, multi-line input, and more.
* [aws4s](https://github.com/aws4s/aws4s) - Non-blocking AWS SDK for Scala exposing strongly-typed APIs built on top of http4s, fs2 and cats.
* [BootZooka ★ 331 ⧗ 5](https://github.com/softwaremill/bootzooka) - Simple project to quickly start developing a web application using AngularJS and Akka HTTP, without the need to write login, user registration etc.
* [Eclair ★ 469](https://github.com/ACINQ/eclair) - ACINQ's Lightning Network implementation written in Scala.  Lightning Network is a second layer protocol built on top of bitcoin to address scalability, privacy, confirmation time and many other issues.
* [Fansi ★ 96 ⧗ 15](https://github.com/lihaoyi/fansi) - Scala/Scala.js library for manipulating Fancy Ansi colored strings
* [GoogleApiScala ★ 5 ⧗ 3](https://github.com/EckerdCollege/google-api-scala) - A simple scala library offering control of Google Drive, Calendar, and the Admin SDK.
* [Google4s ★ 7 ⧗ 3](https://github.com/toknapp/google4s/) - Lean, functional library for Google Cloud Services in Scala (KMS, Cloud Storage, PubSub)
* [mailgun4s ★ 7 ⧗ 4](https://github.com/outr/mailgun4s) - Scala wrapper around the Mailgun API
* [media4s ★ 5 ⧗ 3](https://github.com/outr/media4s) - Scala command-line wrapper around ffmpeg, ffprobe, ImageMagick, and other tools relating to media.
* [Miniboxing](https://github.com/miniboxing/miniboxing-plugin) - A Scala compiler plugin that improves program performance -- [see the project web site](http://scala-miniboxing.org) - Less boxes
* [Openquant ★ 73 ⧗ 0](https://github.com/openquant) - A Scala open source quantitative trading platform
* [Ostinato ★ 27 ⧗ 7](https://github.com/marianogappa/ostinato) - A chess library that runs on the server (Scala) and on the browser (ScalaJS)
* [pdf4s ★ 3 ⧗ 3](https://github.com/outr/pdf4s) - Simplified wrapper to create PDFs in Scala.
* [Play Swagger ★ 174 ⧗ 3](https://github.com/iheartradio/play-swagger) - Automatically create Swagger documentation for your Play REST API
* [powerscala ★ 11 ⧗ 80](https://github.com/outr/powerscala) - Powerful framework providing many useful utilities and features on top of the Scala language.
* [pprint](https://github.com/lihaoyi/pprint) - Pretty-printer for Scala values and types for easier reading and debugging
* **[PureConfig ★ 759 ⧗ 2](https://github.com/pureconfig/pureconfig)** - A boilerplate-free Scala library for loading configuration files.
* [REPLesent ★ 319 ⧗ 5](https://github.com/marconilanna/REPLesent) - A presentation tool built inside the Scala REPL. Runs code straight from your slides with a single keystroke.
* [scala-debugger ★ 52 ⧗ 18](https://github.com/ensime/scala-debugger) - Scala libraries and tooling utilizing the Java Debugger Interface.
* [scala-ssh ★ 186 ⧗ 6](https://github.com/sirthias/scala-ssh) - Remote shell access via SSH for your Scala applications
* [Scalan ★ 81 ⧗ 67](https://github.com/scalan/scalan) - A framework for development of domain-specific compilers in Scala
* [ScalaSTM](https://nbronson.github.io/scala-stm/) - Software Transaction Memory for Scala
* [Scavenger](https://gitlab.com/aossie/Scavenger) - An experimental automated theorem prover.
* [service-chassis](https://github.com/allawala/service-chassis) - A scala chassis to get your applications and services bootstrapped quickly.
* [settler ★ 4 ⧗ 171](https://github.com/lucastorri/settler) - Boilerplate-free typed settings generation in Scala.
* [Simple Scala Config ★ 43 ⧗ 5](https://github.com/ElderResearch/ssc) - Thin, idiomatic Scala wrapper around [Typesafe Config](https://github.com/typesafehub/config) with custom `Reader[T]` suppport.
* [YahooFinanceScala ★ 15 ⧗ 2](https://github.com/openquant/YahooFinanceScala) - Get stock data from Yahoo Finance using Akka http.

## Android

*Scala libraries and wrappers for Android development.*

* **[Android SDK Plugin for SBT ★ 609 ⧗ 1](https://github.com/pfn/android-sdk-plugin)** - An sbt plugin that adds tasks for developing Android applications.
* [Gradle Android Scala Plugin ★ 318 ⧗ 20](https://github.com/saturday06/gradle-android-scala-plugin) - A gradle plugin that allows you to use Scala with Android
* **[Macroid ★ 511 ⧗ 3](https://github.com/47deg/macroid)** - A modular functional UI language for Android.
* **[Scaloid ★ 2065 ⧗ 0](https://github.com/pocorall/scaloid)** - Less painful Android development with Scala.

## HTTP

*Scala libraries and wrappers for HTTP clients.*

* [Akka HTTP ★ 306 ⧗ 1](https://github.com/akka/akka-http) - The Streaming-first HTTP server/module of [Akka](https://github.com/akka/akka).
* [Dispatch ★ 366 ⧗ 6](https://github.com/dispatch/reboot) - Library for asynchronous HTTP interaction. It provides a Scala vocabulary for Java’s [async-http-client](https://github.com/AsyncHttpClient/async-http-client).
* **[Finch.io ★ 1005 ⧗ 3](https://github.com/finagle/finch)** - Purely Functional REST API atop of [Finagle](https://github.com/twitter/finagle).
* [Fintrospect ★ 37 ⧗ 0](http://fintrospect.io) - Implement fast, type-safe HTTP webservices for [Finagle](https://github.com/twitter/finagle).
* **[Http4s ★ 732 ⧗ 3](https://github.com/http4s/http4s)** - A minimal, idiomatic Scala interface for HTTP.
* [jefe ★ 2 ⧗ 105](https://github.com/outr/jefe) - Manages installation, updating, downloading, launching, error reporting, proxying, multi-server management, and much more for your stand-alone and web applications.
* [lolhttp ★ 64 ⧗ 10](https://github.com/criteo/lolhttp) An HTTP & HTTP/2 Server and Client library for Scala.
* [RösHTTP ★ 79 ⧗ 9](https://github.com/hmil/RosHTTP) - A lightweight asynchronous HTTP API built with Scala.js in mind. Supports the JVM and Node.js runtimes as well as most browsers.
* **[scalaj-http ★ 580 ⧗ 0](https://github.com/scalaj/scalaj-http)** - Simple scala wrapper for HttpURLConnection (including OAuth support).
* [Scalaxb ★ 235 ⧗ 18](https://github.com/eed3si9n/scalaxb) - An XML data-binding tool for Scala that supports W3C XML Schema (xsd) and Web Services Description Language (wsdl) as the input file.
* [Spray](http://spray.io/) - Actor-based library for http interaction.
* [sttp](https://github.com/softwaremill/sttp) - The Scala HTTP client you always wanted!
* [Tubesocks ★ 12 ⧗ 174](https://github.com/softprops/tubesocks) - Library supporting bi-directional communication with websocket servers.
* [requests-scala ★ 326](https://github.com/lihaoyi/requests-scala) - A Scala port of the popular Python Requests HTTP client: flexible, intuitive, and straightforward to use.

## Semantic Web

*Scala libraries for interactions with the Web of Data, and other RDF tools.*

* [Banana-RDF ★ 207 ⧗ 26](https://github.com/banana-rdf/banana-rdf) - Scala-friendly abstractions for RDF and Linked Data technologies. Supports Jena, Sesame and native Scala.
* [rdfp ★ 4 ⧗ 50](https://github.com/jannvck/rdfp) - RDF stream processing framework in Scala
* [Scowl ★ 16 ⧗ 36](https://github.com/phenoscape/scowl) - Scala DSL allowing a declarative approach to composing OWL expressions and axioms using the OWL API.

## Metrics and Monitoring

*Scala libraries for gathering metrics and monitoring applications.*

* [Kamon](http://kamon.io) - Gathering metrics from applications built with Akka, Spray and Play! with support for user metrics as well.
* [Metrics-Scala ★ 335](https://github.com/erikvanoosten/metrics-scala) - Scala API for Dropwizard's Metrics library.

## Parsing

*Scala libraries for creating parsers.*

* [atto ★ 148 ⧗ 1](https://github.com/tpolecat/atto) - Pure functional incremental text parsing library for Scala, based on Attoparsec.
* [CLIST ★ 43 ⧗ 24](https://github.com/backuity/clist) - Command Line Interface Scala Toolkit
* [decline ★ 101](https://github.com/bkirwi/decline) - composable command-line parser for Scala, built on Cats
* [Fast Parse ★ 467 ⧗ 1](https://github.com/lihaoyi/fastparse) - Fast to write, Fast running Parsers in Scala
* **[Parboiled2 ★ 502 ⧗ 7](https://github.com/sirthias/parboiled2)** - A Fast Parser Generator for Scala 2.10.3+.
* [Scala Parser Combinators ★ 221 ⧗ 0](https://github.com/scala/scala-parser-combinators) - Scala Standard Parser Combinator Library.
* **[Scopt ★ 678 ⧗ 0](https://github.com/scopt/scopt)** - Simple scala command line options parsing.

## Sbt plugins

*Sbt plugins to make your life easier.*

* [better-monadic-for ★ 371 ⧗ 8](https://github.com/oleg-py/better-monadic-for) - A Scala compiler plugin to give patterns and for-comprehensions the love they deserve
* **[coursier ★ 847 ⧗ 0](https://github.com/alexarchambault/coursier)** - A Scala library to fetch dependencies from Maven / Ivy repositories
* [sbt-api-mappings ★ 38 ⧗ 67](https://github.com/ThoughtWorksInc/sbt-api-mappings) - A Sbt plugin that resolves external API links to common Scala libraries.
* [sbt-assembly ★ 1522](https://github.com/sbt/sbt-assembly) - Deploy fat JARs. Restart processes.
* [sbt-buildinfo ★ 274 ⧗ 1](https://github.com/sbt/sbt-buildinfo) - Generates Scala source from build definition.
* [sbt-classfinder ★ 3 ⧗ 39](https://github.com/ruippeixotog/sbt-classfinder) - Retrieves runtime information about the classes and traits in a project.
* [sbt-dependency-check ★ 108 ⧗ 0](https://github.com/albuch/sbt-dependency-check) - SBT Plugin for OWASP DependencyCheck. Monitor your dependencies and report if there are any publicly known vulnerabilities (e.g. CVEs).
* **[sbt-dependency-graph ★ 731 ⧗ 1](https://github.com/jrudolph/sbt-dependency-graph)** - Create a dependency graph for your project.
* [sbt-docker ★ 422 ⧗ 3](https://github.com/marcuslonnberg/sbt-docker) - Create Docker images directly from sbt
* [sbt-doctest ★ 148](https://github.com/tkawachi/sbt-doctest) - Plugin for sbt that generates tests from examples in ScalaDoc.
* [sbt-ensime ★ 197 ⧗ 11](https://github.com/ensime/ensime-sbt) - Generates .ensime config files for SBT projects [http://ensime.org/build_tools/sbt](http://ensime.org/build_tools/sbt)
* [sbt-groll ★ 87 ⧗ 10](https://github.com/sbt/sbt-groll) - sbt plugin to roll the Git history.
* [sbt-haxe ★ 9 ⧗ 274](https://github.com/qifun/sbt-haxe) - A Sbt plugin to compile Haxe sources.
* [sbt-ide-settings ★ 32 ⧗ 27](https://github.com/Jetbrains/sbt-ide-settings) - SBT plugin for tweaking various IDE settings
* **[sbt-native-packager ★ 811 ⧗ 3](https://github.com/sbt/sbt-native-packager)** - Bundle up Scala software for native packaging systems, like deb, rpm, homebrew, msi..
* [sbt-pack ★ 284 ⧗ 7](https://github.com/xerial/sbt-pack) - A sbt plugin for creating distributable Scala packages.
* [sbt-pantarhei ★ 3 ⧗ 0](https://github.com/kolov/sbt-pantarhei) - SBT plugin to generate release notes from the pull requests and git commits in GitHub.
* **[sbt-revolver ★ 519 ⧗ 0](https://github.com/spray/sbt-revolver)** - Fork & Stop processes from sbt.
* [sbt-robovm ★ 107 ⧗ 17](https://github.com/roboscala/sbt-robovm) - An sbt plugin for iOS development in Scala
* [sbt-scala-js-map ★ 12 ⧗ 2](https://github.com/ThoughtWorksInc/sbt-scala-js-map) - A sbt plugin that configures source mapping for Scala.js projects hosted on Github
* [sbt-sublime ★ 145 ⧗ 38](https://github.com/orrsella/sbt-sublime) - Create Sublime Text projects with library dependencies sources
* [sbt-updates ★ 316 ⧗ 3](https://github.com/rtimush/sbt-updates) - Shows sbt project's dependency updates.
* [sbt-versions ★ 14 ⧗ 167](https://github.com/sksamuel/sbt-versions) - Plugin that checks for updated versions of your project's dependencies.
* [sbt-view ★ 7 ⧗ 18](https://github.com/nestorpersist/sbt-view) - View ScalaDoc/JavaDoc in browser window.
* **[sbteclipse ★ 632 ⧗ 0](https://github.com/typesafehub/sbteclipse)** - Create Eclipse project definitions from sbt builds.
* [scala-clippy ★ 211 ⧗ 5](https://github.com/softwaremill/scala-clippy) - Good advice and coloring for Scala compiler errors
* [ScalaKata2 ★ 79 ⧗ 0](https://github.com/MasseGuillaume/ScalaKata2) - Scala playground & Documentation tool.
* [sbt-hepek ★ 5 ⧗ 0](https://github.com/sake92/sbt-hepek) - Make static websites in Scala code (render `object` to file!).
* [splain ★ 234 ⧗ 0](https://github.com/tek/splain) - Better implicit errors for Scala.
* [tut ★ 364 ⧗ 2](https://github.com/tpolecat/tut) - Tool for writing documentation with typechecked examples.
* [xsbt-web-plugin ★ 334 ⧗ 1](https://github.com/earldouglas/xsbt-web-plugin) - Build enterprise J2EE Web applications in Scala.

## XML / HTML

*XML and HTML generation and processing*

* [scala-scraper ★ 316 ⧗ 1](https://github.com/ruippeixotog/scala-scraper) - A library for scraping content from HTML pages.
* [xs4s ★ 29 ⧗ 47](https://github.com/ScalaWilliam/xs4s) - XML Streaming for Scala for processing large (gigabytes and over) XML files.

## Markdown

* [Laika ★ 161](https://github.com/planet42/Laika) - Text Markup Transformer for sbt and Scala applications, transforming Markdown and reStructuredText to HTML and PDF.

## Learning Scala

*Nice books, blogs and other resources to learn Scala*

### Community Members' Blogs
* http://aperiodic.net/phil/scala/s-99/
* http://appliedscala.com/
* http://blog.higher-order.com/
* http://blog.tmorris.net/tags/Scala/index.html
* http://danielwestheide.com/scala/neophytes.html
* http://debasishg.blogspot.com/
* http://degoes.net/articles/
* http://eed3si9n.com/category/tags/scala
* http://ktoso.github.io/scala-types-of-types/
* http://scalacookbook.com/
* http://scalaprof.blogspot.com/
* http://torre.me.uk/docs/scala/
* http://www.lihaoyi.com/
* http://www.rabbitonweb.com/
* http://www.warski.org/blog/
* https://alvinalexander.com/fpbook
* https://blog.bruchez.name/search/label/scala
* https://github.com/lemastero/scala_typeclassopedia
* https://janzhou.org/scala/
* https://kubuszok.com/tags/#scala
* https://manuel.bernhardt.io/blog/
* https://naildrivin5.com/scalatour/
* https://pchiusano.github.io/
* https://www.beyondthelines.net/

### Company Blogs
* [Functional Works / Learn](https://functional.works-hub.com/learn/) - Quality resources maintained by functional works
* http://allaboutscala.com/
* http://enear.github.io/
* https://blog.knoldus.com/tag/scala/
* https://blog.scalac.io/tags/Scala/
* https://blog.softwaremill.com/tagged/scala
* https://medium.com/disney-streaming/tagged/thisweekinscala
* https://www.codacy.com/blog/
* [Scala Times](https://scalatimes.com/) - Weekly newsletter about scala



### Misc.
* [A Tour of Scala](http://docs.scala-lang.org/tour/tour-of-scala.html) - Bite-sized introductions to some of the core language concepts.
* [CA Art](https://github.com/makingthematrix/ca_art) - A small project aimed at learning Scala on intermediate level by experimenting with Cellular Automata
* **[Demos and Examples in Scala (Chinese) ★ 923 ⧗ 2](https://github.com/jacksu/utils4s)** - repo of sample Scala library usage, written in Chinese
* [Deploying Scala libraries to Sonatype for dummies ★ 23 ⧗ 25](https://github.com/larroy/deployingScalaLibrariesToSonatype) - None
* Resources by [Dr. Mark Lewis](http://www.cs.trinity.edu/~mlewis/) >> [Website](http://www.programmingusingscala.net/) | [Youtube Playlists](https://www.youtube.com/user/DrMarkCLewis/playlists)
* [Exercism - Scala Exercises](http://exercism.io/languages/scala/exercises) - Community-driven Scala exercises.
* [Essential Scala](https://underscore.io/books/essential-scala/) - None
* [Functional Programming in Scala](https://www.coursera.org/specializations/scala) - Coursera Specialization (5 courses) created by  Martin Odersky et al. at the EPFL (Ecole polytechnique fédérale de Lausanne).
* [Functional Programming for Mortals](https://leanpub.com/fpmortals/read) - None
* [Get Programming with Scala](https://www.manning.com/books/get-programming-with-scala) - Tutorial-driven introduction to Scala
* [Introduction to programming with dependent types in Scala](https://stepik.org/course/2294/) - Video Course by Dmytro Mitin
* [Learn-by-doing functional programming course on Scala](https://github.com/dehun/learn-fp/) - Covers type classes, functors, applicatives, monads, monad transformers, free monad
* [Programming Community Curated Resources for Learning Scala](https://hackr.io/tutorials/learn-scala)
* [Reactive Programming with Scala and Akka](http://www.foxebook.net/reactive-programming-with-scala-and-akka/) - Use the concepts of reactive programming to build distributed systems running on multiple nodes
* [Scala Collections Cookbook](http://colobu.com/ScalaCollectionsCookbook/) - Scala collections introduction. written in Chinese.
* [Scala Exercises](http://scala-exercises.47deg.com/) - Brings the popular Scala Koans to the web. Offering hundreds of solvable exercises organized into 42 categories covering the basics of the Scala language.
* [Scala With Cats](https://underscore.io/books/scala-with-cats/) - Learn system architecture and design using the techniques of modern functional programming with [Cats](https://typelevel.org/cats/)
* [Scala in Depth](https://www.manning.com/books/scala-in-depth) - None
* [Scala school](https://twitter.github.io/scala_school/) - Scala school started as a series of lectures at Twitter to prepare experienced engineers to be productive Scala programmers.
* [Scalera Blog](http://www.scalera.es) - Blog about Scala language and its environment (howto's, good practices, tips,...). Weekly posts written in both spanish and english
* [Scala for the Impatient 2nd Edition](https://horstmann.com/scala/) - Covers most Scala features with short and easy to understand explainations.
* [The Type Astronaut's Guide to Shapeless](https://underscore.io/books/shapeless-guide/) - None

## JavaScript

*JavaScript generation and interop libraries.*

* [scala-js-fiddle](http://www.scala-js-fiddle.com/) ([repo](https://github.com/lihaoyi/scala-js-fiddle)) - Browser-based Scala.js playground
* [Scala.js](http://www.scala-js.org/) ([repo](https://github.com/scala-js/scala-js)) - Scala to JavaScript compiler

## Scheduling

* [akka-quartz-scheduler ★ 365](https://github.com/enragedginger/akka-quartz-scheduler) - Quartz Extension and utilities for cron-style scheduling in Akka.

## Templating

*Web templating engines.*

* [Beard ★ 67 ⧗ 3](https://github.com/zalando/beard) - lightweight logicless templating engine inspired by Mustache
* [Scalatags ★ 492 ⧗ 3](https://github.com/lihaoyi/scalatags) - Write html as scala code and have your IDE syntax check it.
* [Scalate ★ 517](https://github.com/scalate/scalate) - Scala based template engine which supports HAML, Mustache and JSP, Erb and Velocity style syntaxes
* [Twirl ★ 324 ⧗ 3](https://github.com/playframework/twirl) - The Play Scala Template Compiler

## Tools

* [Codacy](https://www.codacy.com/) - Automated Code Reviews for Scala
* [dregrex](https://github.com/marianobarrios/dregex) - Regular expression engine using deterministic finite automata. It supports some Perl-style features and yet retains linear matching time.
* [Fastring ★ 97 ⧗ 2](https://github.com/Atry/fastring) - Extremely fast string formatting
* [fast-string-interpolator ★ 24 ⧗ 0](https://github.com/Sizmek/fast-string-interpolator) - Scala macro that generates ultra-fast string interpolators
* **[Gitbucket ★ 6296 ⧗ 0](https://github.com/gitbucket/gitbucket)** - The easily installable GitHub clone powered by Scala
* [Giter8](http://www.foundweekends.org/giter8/) command line tool to generate files and directories from templates published on Github
* [Mill](http://www.lihaoyi.com/mill/) - A better Scala build tool
* [pos ★ 13](https://github.com/JohnReedLOL/pos) - Print debug tool, successor of scala-trace-debug
* [Scalafix](https://github.com/scalacenter/scalafix) - Refactoring and linting tool
* [sbt](http://www.scala-sbt.org/) ([repo](https://github.com/sbt/sbt)) - The interactive build tool for Scala
* [Scala @LibHunt](https://scala.libhunt.com) - The go-to Scala Toolbox.
* [scala-trace-debug ★ 111  ⧗ 14](https://github.com/JohnReedLOL/scala-trace-debug) - Multithreaded print debug tool
* [Scalariform ★ 116 ⧗ 47](https://github.com/daniel-trinh/scalariform) - Scala source code formatter
* [Scalastyle ★ 463 ⧗ 1](https://github.com/scalastyle/scalastyle) - Scala style checker.
* [Scalatex ★ 236 ⧗ 12](https://github.com/lihaoyi/Scalatex) - Programmable, Typesafe Document Generation
* [Scapegoat ★ 230 ⧗ 6](https://github.com/sksamuel/scapegoat) - Scala compiler plugin for static code analysis
* [Scaps](http://scala-search.org/) ([repo](https://github.com/scala-search/scaps)) - A search engine for Scala libraries
* [Scoverage](https://github.com/scoverage) - Scala Code Coverage tool
* **[Wartremover ★ 662 ⧗ 1](https://github.com/puffnfresh/wartremover)** - Wartremover a flexible Scala code linting tool

## Geospatial

*Libraries to aid with geospatial calculations and artifacts.*

* **[Geotrellis ★ 553 ⧗ 0](https://github.com/locationtech/geotrellis)** - Scalable raster toolkit for GIS processing
* [osm4scala ★ 8 ⧗ 40](https://github.com/angelcervera/osm4scala) - OpenStreetMap PBF2 file parser
* [rtree2d ★ 27 ⧗ 1](https://github.com/Sizmek/rtree2d) - RTree2D is a 2D immutable R-tree with STR (Sort-Tile-Recursive) packing for ultra-fast nearest and intersection queries on plane and spherical surfaces
* [sfcurve ★ 20 ⧗ 1](https://github.com/locationtech/sfcurve) - Space filling curves in Scala for geospatial indexing and query

## Devops

*DevOps related tools and libraries.*

* [Skuber ★ 85 ⧗ 0](https://github.com/doriordan/skuber) - Kubernetes client in Scala

# Resources

Where to discover new Scala libraries.

## Podcasts

* [CoRecursive Interviews](https://corecursive.com/) - In-depth Interviews with software developers, often on the subject of scala libraries and functional programming.

# Contributing

Your contributions are always welcome! Please submit a pull request or create an issue to add a new framework, library or software to the list. Do not submit a project that hasn’t been updated in the past 6 months or is not awesome.
