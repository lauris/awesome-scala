
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
    - [Command Line Interfaces](#command-line-interfaces)
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

### Artificial Intelligence

* [CIlib ★ 105 ⧗ 3](https://github.com/cirg-up/cilib) - Typesafe, purely functional Computational Intelligence.
* [CIlib-tutorial ★ 5 ⧗ 166](https://github.com/cirg-up/cilib-tutorial) - A tutorial book for cilib.

### Database

*Database access libraries in Scala.*

* [akka-persistence-gcp-datastore ★ 11 ⧗ 11](https://github.com/innFactory/akka-persistence-gcp-datastore) - akka-persistence-gcp-datastore is a journal and snapshot store plugin for akka-persistence using Google Cloud Datastore.
* [Anorm ★ 196 ⧗ 10](https://github.com/playframework/anorm) - Simple SQL data access.
* **[Casbah ★ 525 ⧗ 5](https://github.com/mongodb/casbah)** - Officially supported Scala driver for MongoDB
* [Clickhouse-scala-client ★ 66 ⧗ 0](https://github.com/crobox/clickhouse-scala-client) - Reactive client for Clickhouse
* [Couchbase ★ 17 ⧗ 0](https://github.com/couchbase/couchbase-jvm-clients) - Official Couchbase client for Scala.
* [CouchDB-Scala ★ 63 ⧗ 263](https://github.com/beloglazov/couchdb-scala) - Purely functional Scala client for CouchDB
* **[doobie ★ 1631 ⧗ 0](https://github.com/tpolecat/doobie)** - Pure functional JDBC layer for Scala.
* **[Elastic4s ★ 1461 ⧗ 0](https://github.com/sksamuel/elastic4s)** - A scala DSL / reactive client for Elasticsearch
* [etcd4s ★ 25 ⧗ 11](https://github.com/mingchuno/etcd4s) - Scala etcd client implementing V3 APIs
* [Finagle ★ 65 ⧗ 2](https://github.com/finagle/finagle-postgres) - PostgreSQL protocol support for Finagle
* [laserdisc ★ 47 ⧗ 2](https://github.com/laserdisc-io/laserdisc) - A Future-free, fs2 native pure FP Redis client
* [longevity ★ 101 ⧗ 17](https://github.com/longevityframework/longevity) - A Persistence Framework for Scala and NoSQL with a Domain Driven Design Orientation
* [lucene4s ★ 39 ⧗ 31](https://github.com/outr/lucene4s) - Light-weight convenience wrapper around Lucene to simplify complex tasks and add Scala sugar.
* [MapperDao ★ 10 ⧗ 680](https://github.com/kostaskougios/mapperdao) - An ORM library for oracle, mysql, mssql, and postgresql
* [Memcontinuationed ★ 52 ⧗ 5](https://github.com/Atry/memcontinuationed) - Memcached client for Scala.
* [Morpheus ★ 102 ⧗ 5](https://github.com/outworkers/morpheus) - Reactive type safe Scala Driver for MySQL/Postgres.
* [neo4akka ★ 16 ⧗ 298](https://github.com/outr/neo4akka) - Neo4j Scala client using Akka HTTP with compile-time query interpolation, case class support, true non-blocking IO, and much more.
* [neotypes ★ 83 ⧗ 14](https://github.com/neotypes/neotypes) - Pure functional driver for neo4j.
* **[Phantom ★ 1037 ⧗ 0](https://github.com/outworkers/phantom)** - Reactive typed Scala driver for Apache Cassandra.
* **[PostgreSQL and MySQL async ★ 1428 ⧗ 0](https://github.com/mauricio/postgresql-async)** - Async database drivers to talk to PostgreSQL and MySQL in Scala.
* [Pulsar4s ★ 132 ⧗ 13](https://github.com/sksamuel/pulsar4s) - Scala client for Apache Pulsar.
* **[Quill ★ 1640 ⧗ 0](https://github.com/getquill/quill)** - Compile-time Language Integrated Query for Scala
* [ReactiveCouchbase ★ 26 ⧗ 182](https://github.com/ReactiveCouchbase/ReactiveCouchbase-rs-core) - Reactive Scala Driver for Couchbase. Also includes a Play plug-in. An official plug-in is also in development.
* **[ReactiveMongo ★ 807 ⧗ 4](https://github.com/ReactiveMongo/ReactiveMongo)** - Reactive Scala Driver for MongoDB.
* **[rediscala ★ 780 ⧗ 5](https://github.com/etaty/rediscala)** - Non-blocking, Reactive Redis driver for Scala (with Sentinel support)
* [Relate ★ 161 ⧗ 5](https://github.com/lucidsoftware/relate) - Lightweight, blazing-fast database access layer for Scala that abstracts the idiosyncricies of the JDBC while keeping complete control over the SQL.
* [Salat ★ 492 ⧗ 5](https://github.com/salat/salat/) - ORM for MongoDB. A related Play-plugin is also available.
* **[Sangria ★ 1680 ⧗ 2](https://github.com/sangria-graphql/sangria)** - Scala GraphQL Implementation
* [Scala ActiveRecord ★ 317 ⧗ 5](https://github.com/aselab/scala-activerecord) - ORM library for scala, inspired by ActiveRecord of Ruby on Rails.
* [Scala-Forklift ★ 168 ⧗ 10](https://github.com/lastland/scala-forklift) - Type-safe database migration for Slick, Git, etc.
* **[scala-redis ★ 957 ⧗ 1](https://github.com/debasishg/scala-redis)** - A Scala library for connecting to a redis server, with clustering support
* [scala-sql ★ 65 ⧗ 5](https://github.com/wangzaixiang/scala-sql) - Yet another SQL-based DB access library for scala language
* [ScalaRelational ★ 54 ⧗ 88](https://github.com/outr/scalarelational) - Type-Safe framework for defining, modifying, and querying SQL databases.
* **[ScalikeJDBC ★ 1080 ⧗ 0](https://github.com/scalikejdbc/scalikejdbc)** - A tidy SQL-based DB access library for Scala developers.
* [Scanamo ★ 254 ⧗ 1](https://github.com/guardian/scanamo) - A library to make using DynamoDB with Scala simpler and less error-prone.
* [scredis ★ 154 ⧗ 67](https://github.com/Livestream/scredis) - Non-blocking Redis client built on top of Akka IO (used by Livestream)
* [Scruid ★ 87 ⧗ 0](https://github.com/ing-bank/scruid) - Scruid (Scala+Druid) is an open source library that allows you to compose Druid queries easily in Scala.
* [Shade ★ 106 ⧗ 124](https://github.com/alexandru/shade) - Memcached client for Scala, based on Spymemcached
* **[Slick ★ 2335 ⧗ 3](https://github.com/slick/slick)** - Modern database query and access library for Scala.
* **[Slick-pg ★ 735 ⧗ 1](https://github.com/tminglei/slick-pg)** - Slick extensions for PostgreSQL.
* [Sorm ★ 238 ⧗ 5](https://github.com/sorm/sorm) - A functional boilerplate-free Scala ORM.
* **[Squeryl ★ 544 ⧗ 3](https://github.com/squeryl/squeryl)** - A Scala DSL for talking with databases with minimum verbosity and maximum type safety.
* [Tepkin ★ 83 ⧗ 5](https://github.com/fehmicansaglam/tepkin) - Reactive MongoDB Driver for Scala built on top of Akka IO and Akka Streams.

### Messaging

* [Op-Rabbit ★ 235 ⧗ 5](https://github.com/SpinGo/op-rabbit) - High-level messaging library for Akka and Op-Rabbit.

### Graphical User Interfaces

*Libraries for creation of graphical user interfaces*

* **[ScalaFX ★ 503 ⧗ 3](https://github.com/scalafx/scalafx)** - Scala DSL for creating Graphical User Interfaces that sits on top of JavaFX.

### Web Frameworks

*Scala frameworks for web development.*

* [Analogweb ★ 12 ⧗ 164](https://github.com/analogweb/analogweb-scala) - Tiny, simple, and pluggable web framework in Scala.
* [Chaos ★ 241 ⧗ 91](https://github.com/mesosphere/chaos) - A lightweight framework for writing REST services in Scala.
* **[Colossus ★ 1152 ⧗ 5](https://github.com/tumblr/colossus)** - lightweight framework for building high-performance applications in Scala that require non-blocking network I/O.
* **[Finatra ★ 1993 ⧗ 0](https://github.com/twitter/finatra)** - A sinatra-inspired web framework for scala, running on top of Finagle.
* **[Lift ★ 1207 ⧗ 2](https://github.com/lift/framework)** - Secure and powerful full stack web framework ([discussion](https://github.com/lauris/awesome-scala/pull/19)).
* [peregine ★ 12 ⧗ 113](https://github.com/dvarelap/peregrine) - A simple and async lightweight Scala web framework.
* **[Play ★ 11555 ⧗ 0](https://github.com/playframework/playframework)** - Makes it easy to build scalable, fast and real-time web applications with Java & Scala.
* [Play Pagelets ★ 75 ⧗ 18](https://github.com/splink/pagelets) - A Module for the Play Framework to build resilient and modular Play applications in an elegant and concise manner.
* [Reactive ★ 207 ⧗ 1](https://github.com/nafg/reactive) - FRP and web abstractions, which can be plugged into any web framework (currently only has bindings for Lift).
* **[scalajs-react ★ 1313 ⧗ 5](https://github.com/japgolly/scalajs-react)** - Facebook's React on Scala.JS.
* **[Scalatra ★ 2445 ⧗ 5](https://github.com/scalatra/scalatra)** - Tiny Scala high-performance, async web framework, inspired by Sinatra.
* **[Skinny Framework ★ 712 ⧗ 3](https://github.com/skinny-framework/skinny-framework)** - A full-stack web app framework upon Scalatra for rapid Development in Scala.
* [suzaku ★ 107 ⧗ 100](https://github.com/suzaku-io/suzaku) - Suzaku web UI framework for Scala
* **[Unfiltered ★ 708 ⧗ 5](https://github.com/unfiltered/unfiltered)** - A modular set of unopinionated primitives for servicing HTTP and WebSocket requests in Scala.
* [Xitrum ★ 449 ⧗ 5](https://github.com/xitrum-framework/xitrum) - An async and clustered Scala web framework and HTTP(S) server fusion on top of Netty, Akka, and Hazelcast.
* [youi ★ 177 ⧗ 8](https://github.com/outr/youi) - Next generation user interface framework and server engine for Scala and Scala.js.

### Reactive Web Frameworks

*Scala libraries for Reactive Web development*

* **[Binding.scala ★ 1482 ⧗ 3](https://github.com/ThoughtWorksInc/Binding.scala)** - A reactive web framework. It enables you use native XML literal syntax to create reactive DOM nodes, which are able to automatically change whenever the data source changes.
* [Korolev ★ 408 ⧗ 3](https://github.com/fomkin/korolev) - Modern single-page applications running on the server side
* [Udash ★ 372 ⧗ 5](https://github.com/UdashFramework/udash-core) - a web framework based on Scala.js with support for property bindings, frontend routing, i18n and much more. It also provides strongly typed client<->server RPC system based on WebSockets.
* [Vert.x Web ★ 85 ⧗ 3](https://github.com/vert-x3/vertx-lang-scala) - Toolkit to build Reactive web applications..
* [Widok ★ 127 ⧗ 224](https://github.com/widok/widok) - Reactive web framework for the JVM and Scala.js

### Data Binding and Validation

*Scala libraries for data binding and validation*

* **[Accord ★ 504 ⧗ 3](https://github.com/wix/accord)** - A sane validation library for Scala
* [Dupin ★ 11 ⧗ 64](https://github.com/yakivy/dupin) - Minimal, idiomatic, customizable validation for Scala.
* [form-binder ★ 20 ⧗ 719](https://github.com/tminglei/form-binder) - A micro data binding and validating framework, very easy to use and hack
* [Monkeytail ★ 85 ⧗ 202](https://github.com/sksamuel/monkeytail) - A set of validation macros and helpers for cats.Validated
* [Octopus ★ 103 ⧗ 4](https://github.com/krzemin/octopus) - Scala library for boilerplate-free validation
* [Veto ★ 2 ⧗ 46](https://github.com/splink/veto) - A scala validation library without dependencies.

### i18n

*Scala libraries for i18n.*

* [scala-xgettext ★ 23 ⧗ 300](https://github.com/xitrum-framework/scala-xgettext) - A compiler plugin that acts like GNU xgettext command to extract i18n strings in Scala source code files to Gettext .po file.
* [Scaposer ★ 35 ⧗ 48](https://github.com/xitrum-framework/scaposer) - GNU Gettext .po file loader for Scala.

### Authentication

*Libraries for implementing authentications schemes.*

* [akka-http-session ★ 413 ⧗ 0](https://github.com/softwaremill/akka-http-session) - Web&mobile client-side sessions for akka-http based applications, with optional JWT support
* [AWS Request Signer ★ 19 ⧗ 47](https://github.com/ticofab/aws-request-signer) - Helper to evaluate the signing headers for HTTP requests to Amazon Web Services.
* [OAuth2-mock-play ★ 24 ⧗ 55](https://github.com/zalando/OAuth2-mock-play) - Implementation of an OAuth2 server designed for mocking/testing and configurable by environment variables (by use of the Typesafe config).
* [Play Google Auth Module ★ 32 ⧗ 4](https://github.com/guardian/play-googleauth) - A very simple implementation of Google OpenID Connect authentication for Play 2 applications.
* [play-pac4j ★ 357 ⧗ 0](https://github.com/pac4j/play-pac4j) - Security library managing authentication (CAS, OAuth, OpenID, SAML, LDAP, SQL, JWT...), authorizations and logout for Play 2.x in Java and Scala.
* **[play-silhouette ★ 802 ⧗ 5](https://github.com/mohiva/play-silhouette)** - Authentication library for Play Framework applications that supports several authentication methods, including OAuth1, OAuth2, OpenID, Credentials or custom authentication schemes.
* **[play2-auth ★ 621 ⧗ 5](https://github.com/t2v/play2-auth)** - Play2.x Authentication and Authorization module.
* **[scala-oauth2-provider ★ 507 ⧗ 8](https://github.com/nulab/scala-oauth2-provider)** - OAuth 2.0 server-side implementation written in Scala.
* **[SecureSocial ★ 1197 ⧗ 3](https://github.com/jaliss/securesocial)** - A module that provides OAuth, OAuth2 and OpenID authentication for Play Framework applications.

### Authorization

*Libraries for implementing authorization strategies.*

* [deadbolt-2 ★ 499 ⧗ 3](https://github.com/schaloner/deadbolt-2) - A Play 2.x module supporting role-based and proprietary authorization; idiomatic APIs for Scala and Java APIs are provided.

### Cryptography

*Cryptography and Encryption Libraries.*

* [Scrypto ★ 164 ⧗ 39](https://github.com/ScorexProject/scrypto) - All-purpose cryptographic framework.
* [TSec ★ 310 ⧗ 10](https://github.com/jmcardon/tsec) - Type-safe, functional, general-cryptography library

### Testing

*Libraries for code testing.*

* [cornichon ★ 202 ⧗ 4](https://github.com/agourlay/cornichon) - Scala DSL for testing HTTP JSON API.
* **[Gatling ★ 4640 ⧗ 0](https://github.com/gatling/gatling)** - Async Scala-Akka-Netty based Stress Tool.
* [Minitest ★ 153 ⧗ 3](https://github.com/monix/minitest) - A testing framework with a focus on simplicity.
* [Mockito Scala ★ 178 ⧗ 7](https://github.com/mockito/mockito-scala) - Mockito for Scala, with improved syntax and many extra features on top of the Java version
* **[ScalaCheck ★ 1614 ⧗ 1](https://github.com/rickynils/scalacheck)** - Property-based testing for Scala.
* [ScalaMeter ★ 460 ⧗ 5](https://github.com/scalameter/scalameter) - Performance &  memory footprint measuring, regression testing.
* [ScalaMock ★ 419 ⧗ 5](https://github.com/paulbutcher/ScalaMock) - Scala native mocking framework
* [scalaprops ★ 254 ⧗ 6](https://github.com/scalaprops/scalaprops) - Another property based testing library for Scala
* **[ScalaTest ★ 885 ⧗ 1](https://github.com/scalatest/scalatest)** - A testing tool for Scala and Java developers.
* [Scalive ★ 204 ⧗ 138](https://github.com/xitrum-framework/scalive) - Connect a Scala REPL to running JVM processes without any prior setup; this library is used for inspecting systems in production mode.
* **[Specs2 ★ 681 ⧗ 4](https://github.com/etorreborre/specs2)** - Software Specifications for Scala.
* [Stryker4s ★ 89 ⧗ 1](https://github.com/stryker-mutator/stryker4s) - Test your tests with mutation testing.
* [testcontainers-scala ★ 301 ⧗ 1](https://github.com/testcontainers/testcontainers-scala) - Docker containers for testing in Scala.
* [µTest ★ 401 ⧗ 20](https://github.com/lihaoyi/utest) - A tiny, portable testing library for Scala.

### JSON

*Libraries for work with json.*

* [argonaut ★ 494 ⧗ 2](https://github.com/argonaut-io/argonaut) - Purely Functional JSON in Scala.
* **[circe ★ 1907 ⧗ 0](https://github.com/travisbrown/circe)** - JSON library based on Argonaut, depends on Cats
* [diffson ★ 228 ⧗ 15](https://github.com/gnieh/diffson) - A scala diff/patch library for Json
* [jackson-module-scala ★ 404 ⧗ 0](https://github.com/FasterXML/jackson-module-scala) - Add-on module for Jackson to support Scala-specific datatypes.
* [jawn ★ 374 ⧗ 5](https://github.com/non/jawn) - Fast json parser (According to them, competetive with java gson/jackson speed).
* **[json4s ★ 1268 ⧗ 0](https://github.com/json4s/json4s)** - Project aims to provide a single AST to be used by other scala json libraries.
* [jsoniter-scala ★ 307 ⧗ 0](https://github.com/plokhotnyuk/jsoniter-scala) - Scala macros for compile-time generation of ultra-fast JSON codecs.
* [persist-json ★ 9 ⧗ 641](https://github.com/nestorpersist/json) - Fast json parser.
* [play-json ★ 229 ⧗ 3](https://github.com/playframework/play-json) - Flexible and powerful JSON manipulation, validation and serialization, with no reflection at runtime.
* [Pushka ★ 75 ⧗ 50](https://github.com/fomkin/pushka) - Scala JSON serialization library with annotations.
* [qbproject ★ 0 ⧗ 1083](https://github.com/ottovw/qbproject) - Scala Libs around JSON and API development for Play Framework.
* [sbt-json ★ 29 ⧗ 276](https://github.com/battermann/sbt-json) - sbt plugin that generates Scala case classes for easy, statically typed and implicit access of JSON documents
* [scala-jsonapi ★ 109 ⧗ 112](https://github.com/scala-jsonapi/scala-jsonapi) - Support library for integrating the JSON API spec with Scala and Spray JSON, Play! JSON or Circe.
* [scalajack ★ 99 ⧗ 27](https://github.com/gzoller/ScalaJack) - Fast 'n easy JSON serialization with optional MongoDB support.  Uses Jackson under the hood.
* **[spray-json ★ 882 ⧗ 0](https://github.com/spray/spray-json)** - Lightweight, clean and efficient JSON implementation in Scala.

### YAML

*Libraries for work with YAML.*

* [MoultingYAML ★ 82 ⧗ 1](https://github.com/jcazevedo/moultingyaml) - Type-class based YAML serialization and deserialization on top of SnakeYAML.

### CSV

*Libraries for work with CSV.*

* [fm-flatfile ★ 10 ⧗ 27](https://github.com/frugalmechanic/fm-flatfile) - Very flexible, Flat File (CSV, TSV, Excel, etc) Reader for Scala.
* [kantan.csv ★ 284 ⧗ 10](https://github.com/nrinaudo/kantan.csv) - CSV handling library for Scala with multiple backends.
* **[Scala-CSV ★ 559 ⧗ 4](https://github.com/tototoshi/scala-csv)** - CSV Reader/Writer for Scala.

### Serialization

*Libraries for serializing and deserializing data for storage or transport.*

* [avro-codegen ★ 7 ⧗ 285](https://github.com/malcolmgreaves/avro-codegen) - Code generation from avro schemas to serialize/deserialize avro messages, no runtime reflection.
* **[Avro4s ★ 516 ⧗ 1](https://github.com/sksamuel/avro4s)** - Avro schema generation and serialization / deserialization for Scala.
* **[Chill ★ 527 ⧗ 5](https://github.com/twitter/chill)** - Extensions for the Kryo serialization library to ease configuration in systems like Hadoop and Storm.
* [msgpack ★ 89 ⧗ 134](https://github.com/msgpack/msgpack-scala) - A efficient binary serialization library.
* **[Pickling ★ 857 ⧗ 5](https://github.com/scala/pickling)** - Fast, customizable, boilerplate-free pickling support.
* [ScalaBuff ★ 223 ⧗ 5](https://github.com/SandroGrzicic/ScalaBuff) - a Scala Protocol Buffers (protobuf) compiler
* **[ScalaPB ★ 971 ⧗ 0](https://github.com/scalapb/ScalaPB)** - Protocol Buffers and gRPC support for Scala
* **[scodec ★ 667 ⧗ 1](https://github.com/scodec/scodec)** - A combinator library for working with binary data.
* **[Scrooge ★ 703 ⧗ 0](https://github.com/twitter/scrooge)** - An Apache Thrift code generator for Scala.
* [validation ★ 194 ⧗ 5](https://github.com/jto/validation) - Advanced validation & serialization for JSON, HTML form data, etc, with no reflection at runtime.
* [µPickle ★ 461 ⧗ 3](https://github.com/lihaoyi/upickle) - A lightweight serialization library for Scala that works in ScalaJS, allowing transfer of structured data between the JVM and JavaScript.

### Science and Data Analysis

*Libraries for scientific computing, data analysis and numerical processing.*

* **[Algebird ★ 1940 ⧗ 3](https://github.com/twitter/algebird)** - Abstract Algebra for Scala.
* [Axle ★ 63 ⧗ 5](https://github.com/axlelang/axle) - A Spire-based DSL for scientific cloud computing.
* **[BigDL ★ 3268 ⧗ 3](https://github.com/intel-analytics/BigDL)** - BigDL is a distributed deep learning library for Apache Spark.
* **[Breeze ★ 3067 ⧗ 1](https://github.com/scalanlp/breeze)** - Breeze is a numerical processing library for Scala.
* [Chalk ★ 264 ⧗ 14](https://github.com/scalanlp/chalk) - Chalk is a natural language processing library.
* [Clustering4Ever ★ 79 ⧗ 3](https://github.com/Clustering4Ever/Clustering4Ever) - Scala and Spark API to benchmark and analyse clustering algorithms on any vectorization you can generate
* [doddle-model ★ 139 ⧗ 26](https://github.com/picnicml/doddle-model) - An in-memory machine learning library built on top of Breeze. It provides immutable objects and exposes its functionality through a scikit-learn-like API.
* **[FACTORIE ★ 555 ⧗ 6](https://github.com/factorie/factorie)** - A toolkit for deployable probabilistic modeling, implemented as a software library in Scala.
* **[Figaro ★ 705 ⧗ 5](https://github.com/p2t2/figaro)** - Figaro is a probabilistic programming language that supports development of very rich probabilistic models.
* [Libra ★ 189 ⧗ 28](https://github.com/to-ithaca/libra) - Libra is a dimensional analysis library based on shapeless, spire and singleton-ops. It contains out of the box support for SI units for all numeric types.
* [LoMRF ★ 69 ⧗ 16](https://github.com/anskarl/LoMRF) - An open-source implementation of Markov Logic Networks in Scala
* [MGO ★ 60 ⧗ 32](https://github.com/openmole/mgo) - Modular multi-objective evolutionary algorithm optimization library enforcing immutability.
* [MLLib](https://spark.apache.org/mllib/) - Machine Learning framework for Spark
* [ND4S ★ 298 ⧗ 68](https://github.com/deeplearning4j/nd4s) - N-Dimensional arrays and linear algebra for Scala with an API similar to Numpy.  ND4S is a scala wrapper around [ND4J](http://nd4j.org/).
* [Numsca ★ 95 ⧗ 31](https://github.com/botkop/numsca) - Numsca is Numpy for Scala.
* [OpenMOLE ★ 115 ⧗ 0](https://github.com/openmole/openmole) - OpenMOLE (Open MOdeL Experiment) is a workflow engine designed to leverage the computing power of distributed execution environments for naturally parallel processes.
* [Optimus ★ 114 ⧗ 123](https://github.com/vagmcs/Optimus) - Optimus is a library for Linear and Quadratic mathematical optimization written in Scala programming language.
* [OscaR](https://bitbucket.org/oscarlib/oscar/wiki/Home) - a Scala toolkit for solving Operations Research problems
* [Persist-Units ★ 9 ⧗ 1109](https://github.com/nestorpersist/units) - Type check units of measure in Scala.
* **[PredictionIO ★ 12321 ⧗ 0](https://github.com/PredictionIO/PredictionIO)** - machine learning server for developers and data scientists. Built on Apache Spark, HBase and Spray
* [Rings ★ 44 ⧗ 13](https://github.com/PoslavskySV/rings) - An efficient library for polynomial rings. Commutative algebra, polynomial GCDs, polynomial factorization and other sci things at a really high speed.
* **[Saddle ★ 506 ⧗ 1](https://github.com/saddle/saddle)** - A minimalist port of Pandas to Scala
* **[Smile ★ 4699 ⧗ 0](https://github.com/haifengl/smile)** - Statistical Machine Intelligence and Learning Engine. Smile is a fast and comprehensive machine learning system.
* **[Spark Notebook ★ 2903 ⧗ 0](https://github.com/andypetrella/spark-notebook)** - Scalable and stable Scala and Spark focused notebook bridging the gap between JVM and Data Scientists (incl. extendable, typesafe and reactive charts).
* **[Spire ★ 1573 ⧗ 0](https://github.com/non/spire)** - Powerful new number types and numeric abstractions for Scala.
* **[Squants ★ 692 ⧗ 6](https://github.com/garyKeorkunian/squants)** - The Scala API for Quantities, Units of Measure and Dimensional Analysis.
* [SwiftLearner ★ 35 ⧗ 66](https://github.com/valdanylchuk/swiftlearner) - Simply written algorithms to help study Machine Learning or write your own implementations.
* [Synapses ★ 31 ⧗ 2](https://github.com/mrdimosthenis/Synapses) - Lightweight Neural Network library, for js, jvm and .net.
* **[Tensorflow_scala ★ 755 ⧗ 1](https://github.com/eaplatanios/tensorflow_scala)** - TensorFlow API for the Scala Programming Language
* [Tyche ★ 97 ⧗ 6](https://github.com/neysofu/tyche) - Probability distributions, stochastic & Markov processes, lattice walks, simple random sampling. A simple yet robust Scala library.
* **[Zeppelin ★ 4619 ⧗ 0](https://github.com/apache/zeppelin)** - Scala and Spark Notebook (like IPython Notebook)

### Big Data

* **[BIDMach ★ 905 ⧗ 7](https://github.com/BIDData/BIDMach)** - CPU and GPU machine learning library, using JNI for GPU computation.
* **[Flink ★ 12367 ⧗ 0](https://github.com/apache/flink)** - Processing framework with powerful stream- and batch-processing capabilities.
* [Gearpump ★ 302 ⧗ 5](https://github.com/apache/incubator-gearpump) - Lightweight real-time big data streaming engine
* [GridScale ★ 21 ⧗ 78](https://github.com/openmole/gridscale) - A Scala API for computing clusters and grids.
* **[Kafka ★ 15225 ⧗ 0](https://github.com/apache/kafka)** - Kafka is a message broker project and aims to provide a unified, high-throughput, low-latency platform for handling real-time data feeds.
* **[Reactive-kafka ★ 1232 ⧗ 0](https://github.com/akka/reactive-kafka)** - Reactive Streams API for Apache Kafka.
* **[Scalding ★ 3226 ⧗ 1](https://github.com/twitter/scalding)** - A Scala binding for the Cascading abstraction of Hadoop MapReduce.
* [Schemer ★ 83 ⧗ 5](https://github.com/indix/schemer) - Schema registry for CSV, TSV, JSON, AVRO and Parquet schema. Supports schema inference and GraphQL API.
* [Scio](https://github.com/spotify/scio) - A Scala API for [Apache Beam](https://beam.apache.org/) and [Google Cloud Dataflow](https://cloud.google.com/dataflow/) - None
* [Scrunch](http://crunch.apache.org/scrunch.html) - A Scala wrapper for [Apache Crunch](http://crunch.apache.org/index.html) which provides a framework for writing, testing, and running MapReduce pipelines.
* **[Spark ★ 25501 ⧗ 0](https://github.com/apache/spark)** - Lightning fast cluster computing — up to 100x faster than Hadoop for iterative algorithms (memory caching) and up to 10x faster than Hadoop for single-pass MapReduce jobs. Compatible with YARN-enabled Hadoop clusters, can run on Mesos and in stand-alone mode as well.
* [spark-deployer ★ 78 ⧗ 176](https://github.com/KKBOX/spark-deployer) - A sbt plugin which helps deploying Apache Spark stand-alone cluster and submitting job on cloud system like AWS EC2.
* [Sparkplug ★ 20 ⧗ 253](https://github.com/indix/sparkplug) - Spark package to "plug" holes in data using SQL based rules
* **[Sparkta ★ 501 ⧗ 2](https://github.com/Stratio/sparkta)** - Real Time Aggregation based on Spark Streaming.
* **[Summingbird ★ 2069 ⧗ 0](https://github.com/twitter/summingbird)** - An implementation of the “lambda architecture” as a software abstraction — a single API for Hadoop and Storm.
* **[Vegas ★ 675 ⧗ 0](https://github.com/vegas-viz/Vegas)** - The missing MatPlotLib for Scala + Spark

### Command Line Interfaces

*Libraries for creation of command line interfaces*

* [CLIST ★ 97 ⧗ 4](https://github.com/backuity/clist) - Command Line Interface Scala Toolkit
* [decline ★ 361 ⧗ 0](https://github.com/bkirwi/decline) - composable command-line parser for Scala, built on Cats
* **[scallop ★ 527 ⧗ 2](https://github.com/scallop/scallop)** - a simple Scala CLI parsing library
* **[Scopt ★ 1195 ⧗ 4](https://github.com/scopt/scopt)** - Simple scala command line options parsing.

### Image processing and image analysis

*2D and 3D image processing and image analysis*

* [scala-phash ★ 14 ⧗ 6](https://github.com/poslegm/scala-phash) - Image comparison by hash codes
* [scalismo ★ 164 ⧗ 0](https://github.com/unibas-gravis/scalismo) - Shape modelling and  model-based image analysis.
* **[scrimage ★ 728 ⧗ 0](https://github.com/sksamuel/scrimage)** - Image io, resize, manipulation and thumbnails.

### Sound processing and music

* [Chromaprint.scala ★ 75 ⧗ 17](https://github.com/mgdigital/Chromaprint.scala) - A Scala implementation of the Chromaprint/AcoustID audio fingerprinting algorithm.
* [ScalaCollider ★ 160 ⧗ 2](https://github.com/Sciss/ScalaCollider) - Sound synthesis and signal processing client for SuperCollider.

### Functional Reactive Programming

*Event streams, signals, observables, etc.*

* **[fs2 ★ 1638 ⧗ 3](https://github.com/functional-streams-for-scala/fs2)** - Compositional, streaming I/O library for Scala
* [Iteratee ★ 179 ⧗ 4](https://github.com/travisbrown/iteratee) - Iteratees for cats
* **[Monix ★ 1654 ⧗ 0](https://github.com/monix/monix)** - Extensions to Scala’s standard library for multi-threading primitives and functional reactive programming. Scala.js compatible.
* [Reactive Collections ★ 3 ⧗ 560](https://github.com/storm-enroute/reactors) - A library that incorporates event streams and signals with specialized collections called reactive containers, and expresses concurrency using isolates and channels.
* [Reactor-Scala-Extensions](https://github.com/reactor/reactor-scala-extensions) - Scala extensions for [Project Reactor ★ 38 ⧗ 2](https://github.com/reactor/reactor-scala-extensions) - None
* [REScala ★ 42 ⧗ 23](https://github.com/rescala-lang/REScala) - REScala is a library for functional reactive programming on the JVM and the Web. It provides a rich API for event stream transformations and signal composition with managed consistent up-to-date state and minimal syntactic overhead.
* **[RxScala ★ 881 ⧗ 5](https://github.com/ReactiveX/RxScala)** - Reactive Extensions for Scala – a library for composing asynchronous and event-based programs using observable sequences
* [scala.frp ★ 23 ⧗ 7](https://github.com/dylemma/scala.frp) - Functional Reactive Programming for Scala (event streams).
* **[Scala.Rx ★ 936 ⧗ 1](https://github.com/lihaoyi/scala.rx)** - An experimental library for Functional Reactive Programming in Scala (reactive variables). Scala.js compatible.
* **[Scalaz ZIO ★ 2100 ⧗ 0](https://github.com/scalaz/scalaz-zio)** - A type-safe, composable library for asynchronous and concurrent programming in Scala
* [SynapseGrid ★ 122 ⧗ 184](https://github.com/Primetalk/SynapseGrid) - an FRP framework for constructing reactive real-time immutable data flow systems. It implements an original way of running and organizing event-driven systems based on Petri nets. The topology can be viewed as a .dot graph. The library is compatible with Akka and can seamlessly communicate with other actors.
* [Vert.x ★ 85 ⧗ 3](https://github.com/vert-x3/vertx-lang-scala) - A polyglot reactive application platform for the JVM which aims to be an alternative to node.js. Its concurrency model resembles actors. It supports [Scala](http://vertx.io/docs/vertx-core/scala/), Clojure, Java, Javascript, Ruby, Groovy and Python.

### Modularization and Dependency Injection

*Modularization of applications, dependency injection, etc.*

* [Airframe ★ 376 ⧗ 0](https://github.com/wvlet/airframe) - Dependency injection library tailored to Scala.
* [Cableguy ★ 1 ⧗ 1339](https://github.com/akozhemiakin/cableguy) - Macro based compile time Dependency Injection library.
* [DIStage ★ 226 ⧗ 0](https://github.com/7mind/izumi) - Staged Dependency Injection with higher-kinded polymorphism and cats/zio support.
* [Grafter ★ 240 ⧗ 13](https://github.com/zalando/grafter) - Grafter is a library to configure and wire Scala applications.
* **[MacWire ★ 1058 ⧗ 0](https://github.com/adamw/macwire)** - Scala Macro to generate wiring code for class instantiation. DI container replacement.
* [Scala-Guice ★ 314 ⧗ 6](https://github.com/codingwell/scala-guice) - Scala extensions for Google Guice
* [Scaldi ★ 281 ⧗ 5](https://github.com/scaldi/scaldi) - Lightweight Scala Dependency Injection Library.
* [Sclasner ★ 9 ⧗ 129](https://github.com/xitrum-framework/sclasner) - Scala classpath scanner.
* [SubCut ★ 400 ⧗ 5](https://github.com/dickwall/subcut) - Scala Uniquely Bound Classes Under Traits.

### Distributed Systems

*Libraries and frameworks for writing distributed applications.*

* **[Akka ★ 10746 ⧗ 0](https://github.com/akka/akka)** - A toolkit and runtime for building highly concurrent, distributed, and fault tolerant event-driven applications.
* [Akka-tracing ★ 309 ⧗ 5](https://github.com/levkhomich/akka-tracing) - A distributed tracing extension for Akka. Provides integration with Play framework, Spray and Akka HTTP.
* [autobreaker ★ 11 ⧗ 13](https://github.com/lucastorri/autobreaker) - Automatically wrap classes that return Futures with a [Circuit Breaker](http://martinfowler.com/bliki/CircuitBreaker.html).
* [Clump ★ 244 ⧗ 5](https://github.com/getclump/clump) - A library for expressive and efficient service composition
* **[CurioDB ★ 504 ⧗ 5](https://github.com/stephenmcd/curiodb)** - Distributed & Persistent Redis Clone built with Scala & Akka.
* **[Finagle ★ 7555 ⧗ 0](https://github.com/twitter/finagle)** - An extensible, protocol-agnostic RPC system designed for high performance and concurrency.
* [Glokka ★ 55 ⧗ 81](https://github.com/xitrum-framework/glokka) - Library to register and lookup actors by names in an Akka cluster.
* **[Lagom ★ 2383 ⧗ 0](https://github.com/lagom/lagom)** - Framework for creating microservice-based systems.
* [Parapet ★ 106 ⧗ 0](https://github.com/parapet-io/parapet) - A purely functional library to build distributed and event-driven systems
* [Reactors ★ 255 ⧗ 5](https://github.com/reactors-io/reactors) - Foundational framework for distributed computing that fuses functional reactive programming and traditional actors.

### Extensions

*Scala extensions.*

* **[Ammonite-Ops ★ 2152 ⧗ 0](https://github.com/lihaoyi/Ammonite)** - Safe, easy, filesystem operations in Scala as convenient as in the Bash shell.
* **[better-files ★ 1330 ⧗ 0](https://github.com/pathikrit/better-files)** - Simple, safe and intuitive Scala I/O. better-files is a dependency-free pragmatic thin Scala wrapper around Java NIO.
* **[Cassovary ★ 982 ⧗ 5](https://github.com/twitter/cassovary)** - A Scala library that is designed from the ground up for space efficiency, handling graphs with billions of nodes and edges.
* **[cats ★ 3832 ⧗ 0](https://github.com/typelevel/cats)** - Lightweight, modular, and extensible library for functional programming.
* **[Chimney ★ 582 ⧗ 0](https://github.com/scalalandio/chimney)** - Scala library for boilerplate-free data transformations.
* [chronoscala ★ 58 ⧗ 8](https://github.com/opt-tech/chronoscala) - Scala wrapper for Java Date/Time API.
* [Dsl.scala ★ 177 ⧗ 12](https://github.com/ThoughtWorksInc/Dsl.scala/) - A framework to create embedded Domain-Specific Languages in Scala, along with some built-in DSLs, including async/await, generators, delimited continuations, asynchronous collection comprehension, RAII, monadic !-notation for cats and scala, etc.
* [Each ★ 234 ⧗ 29](https://github.com/ThoughtWorksInc/each) - A macro library that converts native imperative syntax to [Scalaz](https://github.com/scalaz/scalaz)'s monadic expressions.
* [Eff ★ 445 ⧗ 3](https://github.com/atnos-org/eff) - Extensible effects are an alternative to monad transformers for computing with effects in a functional way.
* [enableIf.scala ★ 57 ⧗ 61](https://github.com/ThoughtWorksInc/enableIf.scala) - A library that switches Scala code at compile-time, like `#if` in C/C++.
* **[Enumeratum ★ 913 ⧗ 2](https://github.com/lloydmeta/enumeratum)** - A macro to replace Scala enumerations with a sealed family of case objects. This allows additional checks for the compiler, e.g. for missing cases in a match statement. Has additinal support for Json libraries and the Play framework.
* [Freasy-Monad ★ 115 ⧗ 205](https://github.com/Thangiee/Freasy-Monad) - Easy way to create Free Monad for Cats and Scalaz using Scala macros with first-class Intellij support.
* [Freedsl ★ 34 ⧗ 398](https://github.com/ISCPIF/freedsl) - A library to implement composable side effects, weaving typeclasses on a wrapping type and the free monad.
* **[Freestyle ★ 613 ⧗ 5](https://github.com/frees-io/freestyle)** - A cohesive & pragmatic framework of FP centric Scala libraries.
* [Hamsters ★ 289 ⧗ 5](https://github.com/scala-hamsters/hamsters) - A mini Scala utility library. Compatible with functional programming beginners. Featuring validation, monad transformers, HLists, Union types.
* [idid ★ 13 ⧗ 281](https://github.com/lucastorri/idid) - A library to define common interfaces for different Id types.
* [Lamma ★ 86 ⧗ 127](https://github.com/maxcellent/lamma) - A Scala date library for date and schedule generation.
* [LArray ★ 339 ⧗ 9](https://github.com/xerial/larray) - Large off-heap arrays (> 2GB) and mmap files.
* [Log4s ★ 144 ⧗ 2](https://github.com/Log4s/log4s) - Fast, Scala-friendly logging bindings on top of [SLF4J](http://slf4j.org/). Uses macros for extreme performance.
* [LogStage ★ 226 ⧗ 0](https://github.com/7mind/izumi) - Zero-effort structural logger for Scala with [SLF4J] integration.
* **[Monocle ★ 1220 ⧗ 1](https://github.com/julien-truffaut/Monocle)** - An Optics/Lens library for purely functional manipulation of immutable objects.
* **[n-scala ★ 823 ⧗ 5](https://github.com/nscala-time/nscala-time)** - Scala wrapper for Joda Time.
* [Persist-Logging ★ 38 ⧗ 36](https://github.com/nestorpersist/logging) - Comprehensive logging library for Scala.
* **[Quicklens ★ 575 ⧗ 4](https://github.com/adamw/quicklens)** - modify deeply nested case class fields with an elegant API
* [Rapture ★ 193 ⧗ 5](https://github.com/propensive/rapture) - a collection of libraries for common, everyday programming tasks (I/O, JSON, i18n, etc.)
* [Records for Scala ★ 156 ⧗ 5](https://github.com/scala-records/scala-records) - Labeled records for Scala based on structural refinement types and macros.
* **[refined ★ 1092 ⧗ 3](https://github.com/fthomas/refined)** - Simple refinement types with compile- and runtime checking
* [Resolvable ★ 3 ⧗ 672](https://github.com/stanch/resolvable) - A library to optimize fetching immutable data structures from several endpoints in several formats.
* **[Scala Async ★ 1023 ⧗ 1](https://github.com/scala/async)** - An asynchronous programming facility for Scala.
* [Scala Graph ★ 493 ⧗ 0](https://github.com/scala-graph/scala-graph) - A Scala library with basic graph functionality that seamlessly fits into the Scala standard collections library.
* **[Scala-Logging ★ 754 ⧗ 1](https://github.com/lightbend/Scala-Logging)** - Convenient and performant logging library for Scala wrapping SLF4J.
* **[scala.meta ★ 829 ⧗ 1](https://github.com/scalameta/scalameta)** - A clean-room implementation of a metaprogramming toolkit for Scala.
* [Scalactic](http://www.scalactic.org/) - Small library of utilities related to quality that helps keeping code clear and correct.
* **[Scalaz ★ 4324 ⧗ 0](https://github.com/scalaz/scalaz)** - An extension to the core Scala library for functional programming.
* [scribe ★ 252 ⧗ 0](https://github.com/outr/scribe) - Practical logging framework that doesn't depend on any other logging framework and can be completely configured programmatically.
* **[Shapeless ★ 2967 ⧗ 0](https://github.com/milessabin/shapeless)** - A type class and dependent type based generic programming library for Scala.
* **[Simulacrum ★ 870 ⧗ 1](https://github.com/mpilquist/simulacrum)** - First class syntax support for type classes in Scala.
* [Squid ★ 157 ⧗ 5](https://github.com/epfldata/squid) - Type-safe metaprogramming framework with typed, hygienic quasiquotes.
* [Stateless Future ★ 179 ⧗ 5](https://github.com/qifun/stateless-future) - Asynchronous programming in fully featured Scala syntax.
* [tinylog ★ 287 ⧗ 0](https://github.com/pmwmedia/tinylog) - Lightweight logging framework with native logging API for Scala.
* **[Twitter Util ★ 2354 ⧗ 0](https://github.com/twitter/util)** - General-purpose Scala libraries, including a future implementation and other concurrency tools.
* [wvlet-log ★ 59 ⧗ 0](https://github.com/wvlet/log) - A library for enhancing your application logs with colors and source code locations.

### Misc

*Projects that don't fit into any specific category.*

* [Agora](https://gitlab.com/aossie/Agora/) - Library of vote-counting algorithms for elections.
* **[Ammonite-REPL ★ 2152 ⧗ 0](https://github.com/lihaoyi/Ammonite)** - An improved Scala REPL: syntax highlighting, output formatting, multi-line input, and more.
* [aws4s ★ 83 ⧗ 11](https://github.com/aws4s/aws4s) - Non-blocking AWS SDK for Scala exposing strongly-typed APIs built on top of http4s, fs2 and cats.
* **[BootZooka ★ 516 ⧗ 0](https://github.com/softwaremill/bootzooka)** - Simple project to quickly start developing a web application using AngularJS and Akka HTTP, without the need to write login, user registration etc.
* **[Eclair ★ 828 ⧗ 0](https://github.com/ACINQ/eclair)** - ACINQ's Lightning Network implementation written in Scala.  Lightning Network is a second layer protocol built on top of bitcoin to address scalability, privacy, confirmation time and many other issues.
* [Fansi ★ 160 ⧗ 4](https://github.com/lihaoyi/fansi) - Scala/Scala.js library for manipulating Fancy Ansi colored strings
* [Google4s ★ 9 ⧗ 88](https://github.com/toknapp/google4s/) - Lean, functional library for Google Cloud Services in Scala (KMS, Cloud Storage, PubSub)
* [GoogleApiScala ★ 17 ⧗ 225](https://github.com/EckerdCollege/google-api-scala) - A simple scala library offering control of Google Drive, Calendar, and the Admin SDK.
* [mailgun4s ★ 11 ⧗ 269](https://github.com/outr/mailgun4s) - Scala wrapper around the Mailgun API
* [media4s ★ 20 ⧗ 37](https://github.com/outr/media4s) - Scala command-line wrapper around ffmpeg, ffprobe, ImageMagick, and other tools relating to media.
* [Miniboxing ★ 107 ⧗ 5](https://github.com/miniboxing/miniboxing-plugin) - A Scala compiler plugin that improves program performance
* [Openquant ★ 19 ⧗ 176](https://github.com/openquant/YahooFinanceScala) - A Scala open source quantitative trading platform
* [Ostinato ★ 36 ⧗ 117](https://github.com/marianogappa/ostinato) - A chess library that runs on the server (Scala) and on the browser (ScalaJS)
* [pdf4s ★ 4 ⧗ 792](https://github.com/outr/pdf4s) - Simplified wrapper to create PDFs in Scala.
* [Play Swagger ★ 347 ⧗ 5](https://github.com/iheartradio/play-swagger) - Automatically create Swagger documentation for your Play REST API
* [powerscala ★ 14 ⧗ 321](https://github.com/outr/powerscala) - Powerful framework providing many useful utilities and features on top of the Scala language.
* [pprint ★ 97 ⧗ 6](https://github.com/lihaoyi/pprint) - Pretty-printer for Scala values and types for easier reading and debugging
* **[PureConfig ★ 945 ⧗ 0](https://github.com/pureconfig/pureconfig)** - A boilerplate-free Scala library for loading configuration files.
* [REPLesent ★ 395 ⧗ 5](https://github.com/marconilanna/REPLesent) - A presentation tool built inside the Scala REPL. Runs code straight from your slides with a single keystroke.
* [scala-debugger ★ 99 ⧗ 31](https://github.com/ensime/scala-debugger) - Scala libraries and tooling utilizing the Java Debugger Interface.
* [scala-ssh ★ 226 ⧗ 5](https://github.com/sirthias/scala-ssh) - Remote shell access via SSH for your Scala applications
* [Scalan ★ 91 ⧗ 5](https://github.com/scalan/scalan) - A framework for development of domain-specific compilers in Scala
* [ScalaSTM ★ 237 ⧗ 5](https://github.com/nbronson/scala-stm) - Software Transaction Memory for Scala
* [Scavenger](https://gitlab.com/aossie/Scavenger) - An experimental automated theorem prover.
* [service-chassis ★ 6 ⧗ 25](https://github.com/allawala/service-chassis) - A scala chassis to get your applications and services bootstrapped quickly.
* [settler ★ 6 ⧗ 342](https://github.com/lucastorri/settler) - Boilerplate-free typed settings generation in Scala.
* [Simple Scala Config ★ 47 ⧗ 234](https://github.com/ElderResearch/ssc) - Thin, idiomatic Scala wrapper around [Typesafe Config](https://github.com/typesafehub/config) with custom `Reader[T]` suppport.
* [YahooFinanceScala ★ 19 ⧗ 176](https://github.com/openquant/YahooFinanceScala) - Get stock data from Yahoo Finance using Akka http.

### Android

*Scala libraries and wrappers for Android development.*

* **[Android SDK Plugin for SBT ★ 746 ⧗ 0](https://github.com/pfn/android-sdk-plugin)** - An sbt plugin that adds tasks for developing Android applications.
* [Gradle Android Scala Plugin ★ 345 ⧗ 37](https://github.com/saturday06/gradle-android-scala-plugin) - A gradle plugin that allows you to use Scala with Android
* **[Macroid ★ 541 ⧗ 5](https://github.com/47deg/macroid)** - A modular functional UI language for Android.
* **[Scaloid ★ 2118 ⧗ 5](https://github.com/pocorall/scaloid)** - Less painful Android development with Scala.

### HTTP

*Scala libraries and wrappers for HTTP clients.*

* **[Akka HTTP ★ 1038 ⧗ 0](https://github.com/akka/akka-http)** - The Streaming-first HTTP server/module of [Akka](https://github.com/akka/akka).
* [Dispatch ★ 433 ⧗ 5](https://github.com/dispatch/reboot) - Library for asynchronous HTTP interaction. It provides a Scala vocabulary for Java’s [async-http-client](https://github.com/AsyncHttpClient/async-http-client).
* **[Finch.io ★ 1459 ⧗ 0](https://github.com/finagle/finch)** - Purely Functional REST API atop of [Finagle](https://github.com/twitter/finagle).
* [Fintrospect ★ 84 ⧗ 25](https://github.com/daviddenton/fintrospect) - Implement fast, type-safe HTTP webservices for [Finagle](https://github.com/twitter/finagle).
* **[Http4s ★ 1795 ⧗ 0](https://github.com/http4s/http4s)** - A minimal, idiomatic Scala interface for HTTP.
* [jefe ★ 4 ⧗ 66](https://github.com/outr/jefe) - Manages installation, updating, downloading, launching, error reporting, proxying, multi-server management, and much more for your stand-alone and web applications.
* [lolhttp ★ 87 ⧗ 100](https://github.com/criteo/lolhttp) - An HTTP & HTTP/2 Server and Client library for Scala.
* [requests-scala ★ 459 ⧗ 1](https://github.com/lihaoyi/requests-scala) - A Scala port of the popular Python Requests HTTP client: flexible, intuitive, and straightforward to use.
* [RösHTTP ★ 125 ⧗ 57](https://github.com/hmil/RosHTTP) - A lightweight asynchronous HTTP API built with Scala.js in mind. Supports the JVM and Node.js runtimes as well as most browsers.
* **[scalaj-http ★ 928 ⧗ 2](https://github.com/scalaj/scalaj-http)** - Simple scala wrapper for HttpURLConnection (including OAuth support).
* [Scalaxb ★ 286 ⧗ 8](https://github.com/eed3si9n/scalaxb) - An XML data-binding tool for Scala that supports W3C XML Schema (xsd) and Web Services Description Language (wsdl) as the input file.
* **[Spray ★ 2546 ⧗ 0](https://github.com/spray/spray)** - Actor-based library for http interaction.
* **[sttp ★ 890 ⧗ 1](https://github.com/softwaremill/sttp)** - The Scala HTTP client you always wanted!
* [Tubesocks ★ 12 ⧗ 767](https://github.com/softprops/tubesocks) - Library supporting bi-directional communication with websocket servers.

### Semantic Web

*Scala libraries for interactions with the Web of Data, and other RDF tools.*

* [Banana-RDF ★ 254 ⧗ 2](https://github.com/banana-rdf/banana-rdf) - Scala-friendly abstractions for RDF and Linked Data technologies. Supports Jena, Sesame and native Scala.
* [rdfp ★ 6 ⧗ 157](https://github.com/jannvck/rdfp) - RDF stream processing framework in Scala
* [Scowl ★ 39 ⧗ 11](https://github.com/phenoscape/scowl) - Scala DSL allowing a declarative approach to composing OWL expressions and axioms using the OWL API.

### Metrics and Monitoring

*Scala libraries for gathering metrics and monitoring applications.*

* [Kamon ★ 4 ⧗ 466](https://github.com/kamon-io/kamon-scala) - Gathering metrics from applications built with Akka, Spray and Play! with support for user metrics as well.
* [Metrics-Scala ★ 410 ⧗ 7](https://github.com/erikvanoosten/metrics-scala) - Scala API for Dropwizard's Metrics library.

### Parsing

*Scala libraries for creating parsers.*

* [atto ★ 309 ⧗ 0](https://github.com/tpolecat/atto) - Pure functional incremental text parsing library for Scala, based on Attoparsec.
* **[Fast Parse ★ 858 ⧗ 0](https://github.com/lihaoyi/fastparse)** - Fast to write, Fast running Parsers in Scala
* **[Parboiled2 ★ 632 ⧗ 5](https://github.com/sirthias/parboiled2)** - A Fast Parser Generator for Scala 2.10.3+.
* [Scala Parser Combinators ★ 460 ⧗ 1](https://github.com/scala/scala-parser-combinators) - Scala Standard Parser Combinator Library.

### Sbt plugins

*Sbt plugins to make your life easier.*

* **[better-monadic-for ★ 547 ⧗ 0](https://github.com/oleg-py/better-monadic-for)** - A Scala compiler plugin to give patterns and for-comprehensions the love they deserve
* [coursier ★ 2 ⧗ 134](https://github.com/alexarchambault/coursier) - A Scala library to fetch dependencies from Maven / Ivy repositories ( Coursier is built-in to SBT since 1.3.0 )
* [mdoc ★ 165 ⧗ 0](https://github.com/scalameta/mdoc) - Typechecked markdown documentation for Scala [https://scalameta.org/mdoc/](https://scalameta.org/mdoc/)
* [sbt-api-mappings ★ 74 ⧗ 5](https://github.com/ThoughtWorksInc/sbt-api-mappings) - A Sbt plugin that resolves external API links to common Scala libraries.
* **[sbt-assembly ★ 1609 ⧗ 0](https://github.com/sbt/sbt-assembly)** - Deploy fat JARs. Restart processes.
* [sbt-buildinfo ★ 457 ⧗ 13](https://github.com/sbt/sbt-buildinfo) - Generates Scala source from build definition.
* [sbt-ci-release ★ 126 ⧗ 5](https://github.com/olafurpg/sbt-ci-release) - sbt plugin to automate Sonatype releases from Travis CI
* [sbt-classfinder ★ 3 ⧗ 5](https://github.com/ruippeixotog/sbt-classfinder) - Retrieves runtime information about the classes and traits in a project.
* [sbt-dependency-check ★ 160 ⧗ 5](https://github.com/albuch/sbt-dependency-check) - SBT Plugin for OWASP DependencyCheck. Monitor your dependencies and report if there are any publicly known vulnerabilities (e.g. CVEs).
* **[sbt-dependency-graph ★ 1157 ⧗ 0](https://github.com/jrudolph/sbt-dependency-graph)** - Create a dependency graph for your project.
* **[sbt-docker ★ 663 ⧗ 5](https://github.com/marcuslonnberg/sbt-docker)** - Create Docker images directly from sbt
* [sbt-doctest ★ 164 ⧗ 18](https://github.com/tkawachi/sbt-doctest) - Plugin for sbt that generates tests from examples in ScalaDoc.
* [sbt-ensime ★ 245 ⧗ 59](https://github.com/ensime/ensime-sbt) - Generates .ensime config files for SBT projects [http://ensime.org/build_tools/sbt](http://ensime.org/build_tools/sbt)
* [sbt-ghpages ★ 89 ⧗ 0](https://github.com/sbt/sbt-ghpages) - git, site and ghpages support for sbt projects.
* [sbt-groll ★ 131 ⧗ 5](https://github.com/sbt/sbt-groll) - sbt plugin to roll the Git history.
* [sbt-haxe ★ 9 ⧗ 1343](https://github.com/qifun/sbt-haxe) - A Sbt plugin to compile Haxe sources.
* [sbt-header ★ 161 ⧗ 5](https://github.com/sbt/sbt-header) - an sbt plugin for creating file headers, e.g. copyright headers
* [sbt-hepek ★ 16 ⧗ 5](https://github.com/sake92/sbt-hepek) - Make static websites in Scala code (render `object` to file!).
* [sbt-ide-settings ★ 43 ⧗ 5](https://github.com/Jetbrains/sbt-ide-settings) - SBT plugin for tweaking various IDE settings
* **[sbt-jmh ★ 650 ⧗ 1](https://github.com/ktoso/sbt-jmh)** - "Trust no one, bench everything." - sbt plugin for JMH (Java Microbenchmark Harness)
* [sbt-microsites ★ 255 ⧗ 3](https://github.com/47deg/sbt-microsites) - An sbt plugin to create awesome microsites for your project [https://47deg.github.io/sbt-microsites/](https://47deg.github.io/sbt-microsites/)
* [sbt-mima-plugin ★ 275 ⧗ 3](https://github.com/lightbend/mima) - A tool for catching binary incompatibility in Scala
* **[sbt-native-packager ★ 1341 ⧗ 0](https://github.com/sbt/sbt-native-packager)** - Bundle up Scala software for native packaging systems, like deb, rpm, homebrew, msi..
* [sbt-pack ★ 411 ⧗ 1](https://github.com/xerial/sbt-pack) - A sbt plugin for creating distributable Scala packages.
* [sbt-pantarhei ★ 10 ⧗ 921](https://github.com/kolov/sbt-pantarhei) - SBT plugin to generate release notes from the pull requests and git commits in GitHub.
* [sbt-pgp ★ 110 ⧗ 39](https://github.com/sbt/sbt-pgp) - PGP plugin for sbt
* **[sbt-release ★ 564 ⧗ 5](https://github.com/sbt/sbt-release)** - A release plugin for sbt
* **[sbt-revolver ★ 736 ⧗ 5](https://github.com/spray/sbt-revolver)** - Fork & Stop processes from sbt.
* [sbt-robovm ★ 110 ⧗ 5](https://github.com/roboscala/sbt-robovm) - An sbt plugin for iOS development in Scala
* [sbt-scala-js-map ★ 24 ⧗ 91](https://github.com/ThoughtWorksInc/sbt-scala-js-map) - A sbt plugin that configures source mapping for Scala.js projects hosted on Github
* [sbt-scalafmt ★ 59 ⧗ 5](https://github.com/scalameta/sbt-scalafmt) - sbt plugin for Scalafmt [https://scalameta.org/scalafmt/](https://scalameta.org/scalafmt/)
* [sbt-scoverage ★ 491 ⧗ 6](https://github.com/scoverage/sbt-scoverage) - A plugin for SBT that integrates the scoverage code coverage library.
* [sbt-site ★ 160 ⧗ 5](https://github.com/sbt/sbt-site) - Site generation for sbt [https://www.scala-sbt.org/sbt-site/](https://www.scala-sbt.org/sbt-site/)
* [sbt-sonatype ★ 238 ⧗ 0](https://github.com/xerial/sbt-sonatype) - A sbt plugin for publishing Scala/Java projects to the Maven central.
* [sbt-sublime ★ 140 ⧗ 35](https://github.com/orrsella/sbt-sublime) - Create Sublime Text projects with library dependencies sources
* [sbt-unidoc ★ 108 ⧗ 18](https://github.com/sbt/sbt-unidoc) - sbt plugin to create a unified API document across projects
* **[sbt-updates ★ 610 ⧗ 5](https://github.com/rtimush/sbt-updates)** - Shows sbt project's dependency updates.
* [sbt-versions ★ 16 ⧗ 635](https://github.com/sksamuel/sbt-versions) - Plugin that checks for updated versions of your project's dependencies.
* [sbt-view ★ 7 ⧗ 1087](https://github.com/nestorpersist/sbt-view) - View ScalaDoc/JavaDoc in browser window.
* **[sbteclipse ★ 725 ⧗ 3](https://github.com/typesafehub/sbteclipse)** - Create Eclipse project definitions from sbt builds.
* [scala-clippy ★ 306 ⧗ 5](https://github.com/softwaremill/scala-clippy) - Good advice and coloring for Scala compiler errors
* [ScalaKata2 ★ 94 ⧗ 53](https://github.com/MasseGuillaume/ScalaKata2) - Scala playground & Documentation tool.
* [splain ★ 314 ⧗ 6](https://github.com/tek/splain) - Better implicit errors for Scala.
* **[tut ★ 597 ⧗ 0](https://github.com/tpolecat/tut)** - Tool for writing documentation with typechecked examples.
* [xsbt-web-plugin ★ 373 ⧗ 1](https://github.com/earldouglas/xsbt-web-plugin) - Build enterprise J2EE Web applications in Scala.

### XML / HTML

*XML and HTML generation and processing*

* **[scala-scraper ★ 580 ⧗ 0](https://github.com/ruippeixotog/scala-scraper)** - A library for scraping content from HTML pages.
* [xs4s ★ 34 ⧗ 3](https://github.com/ScalaWilliam/xs4s) - XML Streaming for Scala for processing large (gigabytes and over) XML files.

### Markdown

* [Laika ★ 234 ⧗ 0](https://github.com/planet42/Laika) - Text Markup Transformer for sbt and Scala applications, transforming Markdown and reStructuredText to HTML and PDF.

### JavaScript

*JavaScript generation and interop libraries.*

* [scala-js-fiddle ★ 83 ⧗ 7](https://github.com/lihaoyi/scala-js-fiddle) - Browser-based Scala.js playground
* **[Scala.js ★ 3900 ⧗ 0](https://github.com/scala-js/scala-js)** - Scala to JavaScript compiler

### Scheduling

* **[akka-quartz-scheduler ★ 512 ⧗ 5](https://github.com/enragedginger/akka-quartz-scheduler)** - Quartz Extension and utilities for cron-style scheduling in Akka.

### Templating

*Web templating engines.*

* [Beard ★ 106 ⧗ 46](https://github.com/zalando/beard) - lightweight logicless templating engine inspired by Mustache
* **[Scalatags ★ 618 ⧗ 5](https://github.com/lihaoyi/scalatags)** - Write html as scala code and have your IDE syntax check it.
* **[Scalate ★ 554 ⧗ 5](https://github.com/scalate/scalate)** - Scala based template engine which supports HAML, Mustache and JSP, Erb and Velocity style syntaxes
* [Twirl ★ 465 ⧗ 5](https://github.com/playframework/twirl) - The Play Scala Template Compiler

### Tools

* [scala-trace-debug ★ 111  ⧗ 14](https://github.com/JohnReedLOL/scala-trace-debug) - Multithreaded print debug tool

* **[bloop ★ 615 ⧗ 0](https://github.com/scalacenter/bloop)** - A fast build server for Scala with a rich ecosystem of build tool and IDE integrations.
* [Codacy ★ 33 ⧗ 6](https://github.com/codacy/codacy-scalameta) - Automated Code Reviews for Scala
* [coursier ★ 2 ⧗ 134](https://github.com/alexarchambault/coursier) - Pure Scala Artifact Fetching. A Scala cli and library to fetch dependencies from Maven / Ivy repositories.
* [dregrex ★ 20 ⧗ 62](https://github.com/marianobarrios/dregex) - Regular expression engine using deterministic finite automata. It supports some Perl-style features and yet retains linear matching time.
* [fast-string-interpolator ★ 59 ⧗ 8](https://github.com/Sizmek/fast-string-interpolator) - Scala macro that generates ultra-fast string interpolators
* [Fastring ★ 121 ⧗ 69](https://github.com/Atry/fastring) - Extremely fast string formatting
* **[Gitbucket ★ 8024 ⧗ 0](https://github.com/gitbucket/gitbucket)** - The easily installable GitHub clone powered by Scala
* **[Giter8 ★ 1538 ⧗ 1](https://github.com/foundweekends/giter8)** - command line tool to generate files and directories from templates published on Github
* **[Metals ★ 1141 ⧗ 0](https://github.com/scalameta/metals)** - Scala language server with rich IDE features
* **[Mill ★ 1297 ⧗ 0](https://github.com/lihaoyi/mill)** - A better Scala build tool
* [pos ★ 19 ⧗ 28](https://github.com/JohnReedLOL/pos) - Print debug tool, successor of scala-trace-debug
* **[sbt ★ 4075 ⧗ 1](https://github.com/sbt/sbt)** - The interactive build tool for Scala
* **[Scalafix ★ 503 ⧗ 0](https://github.com/scalacenter/scalafix)** - Refactoring and linting tool
* [Scalariform ★ 116 ⧗ 5](https://github.com/daniel-trinh/scalariform) - Scala source code formatter
* **[Scalastyle ★ 654 ⧗ 3](https://github.com/scalastyle/scalastyle)** - Scala style checker.
* [Scalatex ★ 281 ⧗ 5](https://github.com/lihaoyi/Scalatex) - Programmable, Typesafe Document Generation
* [Scapegoat ★ 354 ⧗ 1](https://github.com/sksamuel/scapegoat) - Scala compiler plugin for static code analysis
* [Scaps ★ 35 ⧗ 376](https://github.com/scala-search/scaps) - A search engine for Scala libraries
* **[Wartremover ★ 915 ⧗ 4](https://github.com/puffnfresh/wartremover)** - Wartremover a flexible Scala code linting tool

### Geospatial

*Libraries to aid with geospatial calculations and artifacts.*

* **[Geotrellis ★ 962 ⧗ 1](https://github.com/locationtech/geotrellis)** - Scalable raster toolkit for GIS processing
* [osm4scala ★ 36 ⧗ 17](https://github.com/angelcervera/osm4scala) - OpenStreetMap PBF2 file parser
* [rtree2d ★ 76 ⧗ 2](https://github.com/Sizmek/rtree2d) - RTree2D is a 2D immutable R-tree with STR (Sort-Tile-Recursive) packing for ultra-fast nearest and intersection queries on plane and spherical surfaces
* [sfcurve ★ 53 ⧗ 3](https://github.com/locationtech/sfcurve) - Space filling curves in Scala for geospatial indexing and query

### Devops

*DevOps related tools and libraries.*

* [Skuber ★ 245 ⧗ 25](https://github.com/doriordan/skuber) - Kubernetes client in Scala

# Learning Scala

*Nice books, blogs and other resources to learn Scala*

## Community Members' Blogs
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

## Company Blogs
* [Functional Works / Learn](https://functional.works-hub.com/learn/) - Quality resources maintained by functional works
* http://allaboutscala.com/
* http://enear.github.io/
* https://blog.knoldus.com/tag/scala/
* https://blog.scalac.io/tags/Scala/
* https://blog.softwaremill.com/tagged/scala
* https://medium.com/disney-streaming/tagged/thisweekinscala
* https://www.codacy.com/blog/
* [Scala Times](https://scalatimes.com/) - Weekly newsletter about scala

## Misc.
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
* [Clean, intuitive, unintrusive, boilerplate-free Scala API](https://github.com/propensive/rapture/blob/dev/doc/json.md)
* [fast, flexible and intuitive JSON for Scala](http://www.lihaoyi.com/upickle/#uJson)
* [Scala @LibHunt](https://scala.libhunt.com) - The go-to Scala Toolbox.

## Podcasts

* [CoRecursive Interviews](https://corecursive.com/) - In-depth Interviews with software developers, often on the subject of scala libraries and functional programming.

# Contributing

Your contributions are always welcome! Please submit a pull request or create an issue to add a new framework, library or software to the list. Do not submit a project that hasn’t been updated in the past 6 months or is not awesome.
