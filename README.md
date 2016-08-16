Awesome Scala [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
=============

A community driven list of useful Scala libraries, frameworks and software. This is not a catalog of all the libraries, just a starting point for your explorations. Inspired by [awesome-python](https://github.com/vinta/awesome-python). Other amazingly awesome lists can be found in the [awesome-awesomeness](https://github.com/bayandin/awesome-awesomeness) list.

Also awesome is [Scaladex](https://index.scala-lang.org/), the searchable, tagged, and centralized index of Scala libraries.

Projects with over 500 stargazers are in bold.

- [Awesome Scala](#awesome-scala)
    - [Database](#database)
    - [Graphical User Interfaces](#graphical-user-interfaces)
    - [Web Frameworks](#web-frameworks)
    - [Reactive Web Frameworks](#reactive-web-frameworks)
    - [Data Binding and Validation](#data-binding-and-validation)
    - [i18n](#i18n)
    - [Authentication](#authentication)
    - [Authorization](#authorization)
    - [Cryptography](#cryptography)
    - [Testing](#testing)
    - [JSON](#json)
    - [YAML](#yaml)
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
    - [XML / HTML](#xml--html)
    - [Tools](#tools)
    - [Learning Scala](#learning-scala)
    - [JavaScript](#javascript)
- [Contributing](#contributing)

## Database

*Database access libraries in Scala.*

* [Activate ★ 295 ⧗ 5](https://github.com/fwbrasil/activate) - Pluggable object persistence in Scala.
* [Casbah](http://mongodb.github.io/casbah/) ([repo](https://github.com/mongodb/casbah)) - Officially supported Scala driver for MongoDB
* [CouchDB-Scala ★ 52 ⧗ 29](https://github.com/beloglazov/couchdb-scala) - Purely functional Scala client for CouchDB
* **[doobie ★ 521 ⧗ 0](https://github.com/tpolecat/doobie)** - Pure functional JDBC layer for Scala.
* **[Elastic4s ★ 664 ⧗ 0](https://github.com/sksamuel/elastic4s)** - A scala DSL / reactive client for Elasticsearch
* [longevity ★ 29 ⧗ 0](https://github.com/longevityframework/longevity) - A Persistence Framework for Scala and NoSQL with a Domain Driven Design Orientation
* [MapperDao ★ 10 ⧗ 15](https://github.com/kostaskougios/mapperdao) - An ORM library for oracle, mysql, mssql, and postgresql
* [Memcontinuationed ★ 50 ⧗ 10](https://github.com/Atry/memcontinuationed) - Memcached client for Scala.
* [Morpheus ★ 15 ⧗ 23](https://github.com/websudos/morpheus) - Reactive type safe Scala Driver for MySQL/Postgres.
* [Phantom ★ 443 ⧗ 3](https://github.com/websudos/phantom) - Reactive type safe Scala driver for Apache Cassandra.
* **[PostgreSQL and MySQL async ★ 840 ⧗ 1](https://github.com/mauricio/postgresql-async)** - Async database drivers to talk to PostgreSQL and MySQL in Scala.
* **[Quill ★ 631 ⧗ 77](https://github.com/getquill/quill)** - Compile-time Language Integrated Query for Scala
* [ReactiveCouchbase](http://reactivecouchbase.org/) - Reactive Scala Driver for Couchbase. Also includes a Play plug-in. An official plug-in is also in development.
* **[ReactiveMongo ★ 661 ⧗ 3](https://github.com/ReactiveMongo/ReactiveMongo)** - Reactive Scala Driver for MongoDB.
* [ReactiveNeo ★ 47 ⧗ 31](https://github.com/websudos/reactiveneo) - Reactive type-safe Scala driver for Neo4J.
* **[rediscala ★ 557 ⧗ 0](https://github.com/etaty/rediscala)** - Non-blocking, Reactive Redis driver for Scala (with Sentinel support)
* [Relate ★ 94 ⧗ 19](https://github.com/lucidsoftware/relate) - Lightweight, blazing-fast database access layer for Scala that abstracts the idiosyncricies of the JDBC while keeping complete control over the SQL.
* [rethink-scala ★ 94 ⧗ 21](https://github.com/kclay/rethink-scala) - Scala Driver for RethinkDB
* [Salat ★ 477 ⧗ 10](https://github.com/salat/salat/) - ORM for MongoDB. A related Play-plugin is also available.
* [Scala ActiveRecord ★ 273 ⧗ 0](https://github.com/aselab/scala-activerecord) - ORM library for scala, inspired by ActiveRecord of Ruby on Rails.
* [Scala-Forklift](https://github.com/lastland/scala-forklift) - Type-safe database migration for Slick, Git, etc.
* **[scala-redis ★ 656 ⧗ 1](https://github.com/debasishg/scala-redis)** - A Scala library for connecting to a redis server, with clustering support
* [scala-sql ★ 11 ⧗ 36](https://github.com/wangzaixiang/scala-sql) - Yet another SQL-based DB access library for scala language
* **[ScalikeJDBC ★ 633 ⧗ 0](https://github.com/scalikejdbc/scalikejdbc)** - A tidy SQL-based DB access library for Scala developers.
* [scredis ★ 147 ⧗ 34](https://github.com/Livestream/scredis) - Non-blocking Redis client built on top of Akka IO (used by Livestream)
* **[Slick ★ 1598 ⧗ 1](https://github.com/slick/slick)** - Modern database query and access library for Scala.
* [Sorm ★ 220 ⧗ 2](https://github.com/sorm/sorm) - A functional boilerplate-free Scala ORM.
* [Squeryl ★ 463 ⧗ 0](https://github.com/squeryl/squeryl) - A Scala DSL for talking with databases with minimum verbosity and maximum type safety.
* [Tepkin ★ 85 ⧗ 104](https://github.com/fehmicansaglam/tepkin) - Reactive MongoDB Driver for Scala built on top of Akka IO and Akka Streams.

## Messaging

* [Op-Rabbit ★ 113 ⧗ 7](https://github.com/SpinGo/op-rabbit) - High-level messaging library for Akka and Op-Rabbit.

## Graphical User Interfaces

*Libraries for creation of graphical user interfaces*

* [ScalaFX](http://www.scalafx.org/) - Scala DSL for creating Graphical User Interfaces that sits on top of JavaFX.

## Web Frameworks

*Scala frameworks for web development.*

* [Analogweb](http://analogweb.org/) - Tiny, simple, and pluggable web framework in Scala.
* [Chaos ★ 200 ⧗ 9](https://github.com/mesosphere/chaos) - A lightweight framework for writing REST services in Scala.
* **[Colossus ★ 811 ⧗ 70](http://tumblr.github.io/colossus/)** - lightweight framework for building high-performance applications in Scala that require non-blocking network I/O.
* **[Finatra ★ 1313 ⧗ 0](https://github.com/twitter/finatra)** - A sinatra-inspired web framework for scala, running on top of Finagle.
* **[Lift ★ 1022 ⧗ 4](https://github.com/lift/framework)** - Secure and powerful full stack web framework ([discussion](https://github.com/lauris/awesome-scala/pull/19)).
* [peregine ★ 10 ⧗ 3](https://github.com/dvarelap/peregrine) - A simple and async lightweight Scala web framework.
* **[Play ★ 8166 ⧗ 0](https://github.com/playframework/playframework)** - Makes it easy to build scalable, fast and real-time web applications with Java & Scala.
* [Reactive ★ 194 ⧗ 10](https://github.com/nafg/reactive) - FRP and web abstractions, which can be plugged into any web framework (currently only has bindings for Lift).
* **[Scalatra ★ 1997 ⧗ 2](https://github.com/scalatra/scalatra)** - Tiny Scala high-performance, async web framework, inspired by Sinatra.
* **[Skinny Framework ★ 570 ⧗ 1](https://github.com/skinny-framework/skinny-framework)** - A full-stack web app framework upon Scalatra for rapid Development in Scala.
* [Socko](http://sockoweb.org/) - An embedded Scala web server powered by Netty networking and Akka processing.
* **[Spray ★ 2380 ⧗ 566](https://github.com/spray/spray)** - A suite of scala libraries for building and consuming RESTful web services on top of Akka.
* **[Unfiltered ★ 642 ⧗ 3](https://github.com/unfiltered/unfiltered)** - A modular set of unopinionated primitives for servicing HTTP and WebSocket requests in Scala.
* [Xitrum](http://xitrum-framework.github.io/) - An async and clustered Scala web framework and HTTP(S) server fusion on top of Netty, Akka, and Hazelcast.

## Reactive Web Frameworks

*Scala libraries for Reactive Web development*

* [Binding.scala ★ 161 ⧗ 0](https://github.com/ThoughtWorksInc/Binding.scala) - A reactive web framework. It enables you use native XML literal syntax to create reactive DOM nodes, which are able to automatically change whenever the data source changes.
* [Udash](http://udash.io/) - a web framework based on Scala.js with support for property bindings, frontend routing, i18n and much more. It also provides strongly typed client<->server RPC system based on WebSockets. 
* [Widok](https://widok.github.io/) - Reactive web framework for the JVM and Scala.js

## Data Binding and Validation

*Scala libraries for data binding and validation*

* [form-binder ★ 15 ⧗ 44](https://github.com/tminglei/form-binder) - A micro data binding and validating framework, very easy to use and hack
* [Accord](https://github.com/wix/accord) - A sane validation library for Scala

## i18n

*Scala libraries for i18n.*

* [scala-xgettext ★ 16 ⧗ 64](https://github.com/xitrum-framework/scala-xgettext) - A compiler plugin that acts like GNU xgettext command to extract i18n strings in Scala source code files to Gettext .po file.
* [Scaposer ★ 27 ⧗ 133](https://github.com/xitrum-framework/scaposer) - GNU Gettext .po file loader for Scala.

## Authentication

*Libraries for implementing authentications schemes.*

* [akka-http-session ★ 191 ⧗ 11](https://github.com/softwaremill/akka-http-session) - Web&mobile client-side sessions for akka-http based applications, with optional JWT support
* [AWS Request Signer](https://github.com/ticofab/aws-request-signer) - Helper to evaluate the signing headers for HTTP requests to Amazon Web Services.
* [play-pac4j ★ 225 ⧗ 17](https://github.com/pac4j/play-pac4j) - Security library managing authentication (CAS, OAuth, OpenID, SAML, LDAP, SQL, JWT...), authorizations and logout for Play 2.x in Java and Scala.
* [play-silhouette ★ 488 ⧗ 0](https://github.com/mohiva/play-silhouette) - Authentication library for Play Framework applications that supports several authentication methods, including OAuth1, OAuth2, OpenID, Credentials or custom authentication schemes.
* **[play2-auth ★ 583 ⧗ 6](https://github.com/t2v/play2-auth)** - Play2.x Authentication and Authorization module.
* [scala-oauth2-provider ★ 356 ⧗ 0](https://github.com/nulab/scala-oauth2-provider) - OAuth 2.0 server-side implementation written in Scala.
* **[SecureSocial ★ 1180 ⧗ 0](https://github.com/jaliss/securesocial)** - A module that provides OAuth, OAuth2 and OpenID authentication for Play Framework applications.

## Authorization

*Libraries for implementing authorization strategies.*

* [deadbolt-2 ★ 417 ⧗ 10](https://github.com/schaloner/deadbolt-2) - A Play 2.x module supporting role-based and proprietary authorization; idiomatic APIs for Scala and Java APIs are provided.

## Cryptography

*Cryptography and Encryption Libraries.*

* [Scrypto ★ 21 ⧗ 7](https://github.com/ScorexProject/scrypto) - All-purpose cryptographic framework.

## Testing

*Libraries for code testing.*

* [Gatling](http://gatling.io) - Async Scala-Akka-Netty based Stress Tool.
* **[ScalaCheck ★ 1030 ⧗ 3](https://github.com/rickynils/scalacheck)** - Property-based testing for Scala.
* [ScalaMeter](https://scalameter.github.io/) - Performance &  memory footprint measuring, regression testing.
* [ScalaMock](http://scalamock.org) - Scala native mocking framework
* [scalaprops ★ 128 ⧗ 1](https://github.com/scalaprops/scalaprops) - Another property based testing library for Scala
* [ScalaTest ★ 428 ⧗ 0](https://github.com/scalatest/scalatest) - A testing tool for Scala and Java developers.
* [Scalive ★ 133 ⧗ 2](https://github.com/xitrum-framework/scalive) - Connect a Scala REPL to running JVM processes without any prior setup; this library is used for inspecting systems in production mode.
* **[Specs2 ★ 521 ⧗ 1](https://github.com/etorreborre/specs2)** - Software Specifications for Scala.
* [µTest ★ 167 ⧗ 21](https://github.com/lihaoyi/utest) - A tiny, portable testing library for Scala.

## JSON

*Libraries for work with json.*

* [argonaut](http://argonaut.io/) - Purely Functional JSON in Scala.
* **[circe ★ 503 ⧗ 1](https://github.com/travisbrown/circe)** - JSON library based on Argonaut, depends on Cats
* [jackson-module-scala ★ 276 ⧗ 7](https://github.com/FasterXML/jackson-module-scala) - Add-on module for Jackson to support Scala-specific datatypes.
* [jawn ★ 206 ⧗ 12](https://github.com/non/jawn) - Fast json parser (According to them, competetive with java gson/jackson speed).
* **[json4s ★ 707 ⧗ 0](https://github.com/json4s/json4s)** - Project aims to provide a single AST to be used by other scala json libraries.
* [persist-json ★ 7 ⧗ 170](https://github.com/nestorpersist/json) - Fast json parser.
* [play-json](https://github.com/playframework/playframework/tree/master/framework/src/play-json) - Flexible and powerful JSON manipulation, validation and serialization, with no reflection at runtime.
* [qbproject ★ 10 ⧗ 90](https://github.com/qb-project/qbproject) - Scala Libs around JSON and API developement for Play Framework.
* [scala-jsonapi ★ 48 ⧗ 2](https://github.com/zalando/scala-jsonapi) - Support library for integrating the JSON API spec with Scala and Spray JSON, Play! JSON or Circe.
* [scalajack ★ 74 ⧗ 96](https://github.com/gzoller/ScalaJack) - Fast 'n easy JSON serialization with optional MongoDB support.  Uses Jackson under the hood.
* [sonofjson ★ 21 ⧗ 13](https://github.com/wspringer/sonofjson) - A Scala library for dealing with JSON in a way that makes it almost feel native.
* **[spray-json ★ 530 ⧗ 3](https://github.com/spray/spray-json)** - Lightweight, clean and efficient JSON implementation in Scala.

## YAML

*Libraries for work with YAML.*

* [MoultingYAML ★ 20 ⧗ 23](https://github.com/jcazevedo/moultingyaml) - Type-class based YAML serialization and deserialization on top of SnakeYAML.

## Serialization

*Libraries for serializing and deserializing data for storage or transport.*

* [avro-codegen ★ 20 ⧗ 7](https://github.com/Nitro/avro-codegen) - Code generation from avro schemas to serialize/deserialize avro messages, no runtime reflection.
* [Chill ★ 349 ⧗ 0](https://github.com/twitter/chill) - Extensions for the Kryo serialization library to ease configuration in systems like Hadoop and Storm.
* **[Pickling ★ 776 ⧗ 1](https://github.com/scala/pickling)** - Fast, customizable, boilerplate-free pickling support.
* [ScalaBuff ★ 209 ⧗ 0](https://github.com/SandroGrzicic/ScalaBuff) - a Scala Protocol Buffers (protobuf) compiler
* [ScalaPB](http://trueaccord.github.io/ScalaPB/) - A Protocol Buffer generator for Scala.
* [scodec ★ 409 ⧗ 5](https://github.com/scodec/scodec) - A combinator library for working with binary data.
* [Scrooge](http://twitter.github.io/scrooge/) - An Apache Thrift code generator for Scala.
* [validation ★ 150 ⧗ 2](https://github.com/jto/validation) - Advanced validation & serialization for JSON, HTML form data, etc, with no reflection at runtime.
* [µPickle](http://lihaoyi.github.io/upickle-pprint/upickle/) - A lightweight serialization library for Scala that works in ScalaJS, allowing transfer of structured data between the JVM and JavaScript.

## Science and Data Analysis

*Libraries for scientific computing, data analysis and numerical processing.*

* **[Algebird ★ 1287 ⧗ 0](https://github.com/twitter/algebird)** - Abstract Algebra for Scala.
* [Axle](http://axle-lang.org) - Spire-based DSL for scientific cloud computing.
* **[Breeze ★ 1642 ⧗ 0](https://github.com/scalanlp/breeze)** - Breeze is a numerical processing library for Scala.
* [Chalk ★ 206 ⧗ 13](https://github.com/scalanlp/chalk) - Chalk is a natural language processing library.
* [FACTORIE ★ 426 ⧗ 0](https://github.com/factorie/factorie) - A toolkit for deployable probabilistic modeling, implemented as a software library in Scala.
* [Figaro ★ 355 ⧗ 0](https://github.com/p2t2/figaro) - Figaro is a probabilistic programming language that supports development of very rich probabilistic models.
* [MGO ★ 13 ⧗ 4](https://github.com/openmole/mgo) - Modular multi-objective evolutionary algorithm optimization library enforcing immutability.
* [MLLib](https://spark.apache.org/mllib/) - Machine Learning framework for Spark
* [ND4S ★ 140 ⧗ 5](https://github.com/deeplearning4j/nd4s) - N-Dimensional arrays and linear algebra for Scala with an API similar to Numpy.  ND4S is a scala wrapper around [ND4J](http://nd4j.org/).
* [OpenMOLE](https://github.com/ISCPIF/openmole) - OpenMOLE (Open MOdeL Experiment) is a workflow engine designed to leverage the computing power of distributed execution environments for naturally parallel processes.
* [OscaR](https://bitbucket.org/oscarlib/oscar/wiki/Home) - a Scala toolkit for solving Operations Research problems
* [Persist-Units ★ 7 ⧗ 64](https://github.com/nestorpersist/units) - Type check units of measure in Scala.
* **[PredictionIO ★ 9446 ⧗ 0](https://github.com/PredictionIO/PredictionIO)** - machine learning server for developers and data scientists. Built on Apache Spark, HBase and Spray
* [Saddle ★ 392 ⧗ 12](https://github.com/saddle/saddle) - A minimalist port of Pandas to Scala
* [Smile](http://haifengl.github.io/smile/) - Statistical Machine Intelligence and Learning Engine. Smile is a fast and comprehensive machine learning system.
* **[Spark Notebook ★ 1439 ⧗ 0](https://github.com/andypetrella/spark-notebook)** - Scalable and stable Scala and Spark focused notebook bridging the gap between JVM and Data Scientists (incl. extendable, typesafe and reactive charts).
* **[Spire ★ 983 ⧗ 0](https://github.com/non/spire)** - Powerful new number types and numeric abstractions for Scala.
* [Squants ★ 283 ⧗ 7](https://github.com/garyKeorkunian/squants) - The Scala API for Quantities, Units of Measure and Dimensional Analysis.
* [Zeppelin](http://zeppelin-project.org/) - Scala and Spark Notebook (like IPython Notebook)

## Big Data

* **[BIDMach ★ 629 ⧗ 0](https://github.com/BIDData/BIDMach)** - CPU and GPU machine learning library, using JNI for GPU computation.
* **[Gearpump ★ 558 ⧗ 1](https://github.com/gearpump/gearpump)** - Lightweight real-time big data streaming engine
* [GridScale ★ 12 ⧗ 189](https://github.com/openmole/gridscale) - A Scala API for computing clusters and grids.
* **[Kafka ★ 3533 ⧗ 0](https://github.com/apache/kafka)** - Kafka is a message broker project and aims to provide a unified, high-throughput, low-latency platform for handling real-time data feeds.
* **[Reactive-kafka ★ 578 ⧗ 0](https://github.com/akka/reactive-kafka)** - Reactive Streams API for Apache Kafka.
* **[Scalding ★ 2586 ⧗ 1](https://github.com/twitter/scalding)** - A Scala binding for the Cascading abstraction of Hadoop MapReduce.
* [Scoobi ★ 484 ⧗ 12](https://github.com/nicta/scoobi) - Write type-safe Hadoop programs in idiomatic Scala way
* [Scoozie ★ 66 ⧗ 8](https://github.com/klout/scoozie) - Scala DSL on top of Oozie XML
* [Scrunch](http://crunch.apache.org/scrunch.html) - A Scala wrapper for [Apache Crunch](http://crunch.apache.org/index.html) which provides a framework for writing, testing, and running MapReduce pipelines.
* [Shadoop ★ 8 ⧗ 329](https://github.com/adamretter/shadoop) - A Scala DSL for Hadoop MapReduce.
* [Spark](http://spark.apache.org/) - Lightning fast cluster computing — up to 100x faster than Hadoop for iterative algorithms (memory caching) and up to 10x faster than Hadoop for single-pass MapReduce jobs. Compatible with YARN-enabled Hadoop clusters, can run on Mesos and in stand-alone mode as well.
* [spark-deployer ★ 62 ⧗ 8](https://github.com/KKBOX/spark-deployer) - A sbt plugin which helps deploying Apache Spark stand-alone cluster and submitting job on cloud system like AWS EC2.
* [Sparkta ★ 235 ⧗ 5](https://github.com/Stratio/sparkta) - Real Time Aggregation based on Spark Streaming.
* **[Summingbird ★ 1764 ⧗ 0](https://github.com/twitter/summingbird)** - An implementation of the “lambda architecture” as a software abstraction — a single API for Hadoop and Storm.

## Image processing and image analysis

*2D and 3D image processing and image analysis*

* [scalismo ★ 31 ⧗ 4](https://github.com/unibas-gravis/scalismo) - Shape modelling and  model-based image analysis.
* [scrimage ★ 384 ⧗ 2](https://github.com/sksamuel/scrimage) - Image io, resize, manipulation and thumbnails.

## Sound processing and music

* [ScalaCollider ★ 100 ⧗ 42](https://github.com/Sciss/ScalaCollider) - Sound synthesis and signal processing client for SuperCollider.

## Functional Reactive Programming

*Event streams, signals, observables, etc.*

* [Monix ★ 464 ⧗ 0](https://github.com/monifu/monix) - Extensions to Scala’s standard library for multi-threading primitives and functional reactive programming. Scala.js compatible.
* [Reactive Collections ★ 2 ⧗ 26](https://github.com/storm-enroute/reactors) - A library that incorporates event streams and signals with specialized collections called reactive containers, and expresses concurrency using isolates and channels.
* **[RxScala ★ 505 ⧗ 0](https://github.com/ReactiveX/RxScala)** - Reactive Extensions for Scala – a library for composing asynchronous and event-based programs using observable sequences
* [scala.frp ★ 18 ⧗ 72](https://github.com/dylemma/scala.frp) - Functional Reactive Programming for Scala (event streams).
* **[Scala.Rx ★ 684 ⧗ 6](https://github.com/lihaoyi/scala.rx)** - An experimental library for Functional Reactive Programming in Scala (reactive variables). Scala.js compatible.
* [SynapseGrid ★ 90 ⧗ 91](https://github.com/Primetalk/SynapseGrid) - an FRP framework for constructing reactive real-time immutable data flow systems. It implements an original way of running and organizing event-driven systems based on Petri nets. The topology can be viewed as a .dot graph. The library is compatible with Akka and can seamlessly communicate with other actors.
* [Vertx.io](http://vertx.io/) - A polyglot reactive application platform for the JVM which aims to be an alternative to node.js. Its concurrency model resembles actors. It supports [Scala](http://vertx.io/core_manual_scala.html), Clojure, Java, Javascript, Ruby, Groovy and Python.

## Modularization and Dependency Injection

*Modularization of applications, dependency injection, etc.*

* [Cableguy ★ 1 ⧗ 3](https://github.com/akozhemiakin/cableguy) - Macro based compile time Dependency Injection library.
* [Domino ★ 2 ⧗ 197](https://github.com/helgoboss/domino) - Write elegant OSGi bundle activators in Scala.
* **[MacWire ★ 518 ⧗ 0](https://github.com/adamw/macwire)** - Scala Macro to generate wiring code for class instantiation. DI container replacement.
* [Scala-Guice ★ 169 ⧗ 1](https://github.com/codingwell/scala-guice) - Scala extensions for Google Guice
* [Scaldi ★ 216 ⧗ 14](https://github.com/scaldi/scaldi) - Lightweight Scala Dependency Injection Library.
* [Sclasner ★ 9 ⧗ 245](https://github.com/xitrum-framework/sclasner) - Scala classpath scanner.
* [SubCut ★ 397 ⧗ 6](https://github.com/dickwall/subcut) - Scala Uniquely Bound Classes Under Traits.

## Distributed Systems

*Libraries and frameworks for writing distributed applications.*

* [Akka](http://akka.io/) - A toolkit and runtime for building highly concurrent, distributed, and fault tolerant event-driven applications.
* [Akka-tracing ★ 212 ⧗ 0](https://github.com/levkhomich/akka-tracing) - A distributed tracing extension for Akka. Provides integration with Play framework, Spray and Akka HTTP.
* [Clump](http://getclump.io) - A library for expressive and efficient service composition
* [CurioDB ★ 424 ⧗ 2](https://github.com/stephenmcd/curiodb) - Distributed & Persistent Redis Clone built with Scala & Akka.
* [Finagle](https://twitter.github.io/finagle/) - An extensible, protocol-agnostic RPC system designed for high performance and concurrency.
* [Glokka ★ 46 ⧗ 29](https://github.com/xitrum-framework/glokka) - Library to register and lookup actors by names in an Akka cluster.
* [Lagom](https://www.lightbend.com/lagom) - Framework for creating microservice-based systems.

## Extensions

*Scala extensions.*

* [Ammonite-Ops](http://lihaoyi.github.io/Ammonite/#Ammonite-Ops) - Safe, easy, filesystem operations in Scala as convenient as in the Bash shell.
* **[better-files ★ 580 ⧗ 0](https://github.com/pathikrit/better-files)** - Simple, safe and intuitive Scala I/O. better-files is a dependency-free pragmatic thin Scala wrapper around Java NIO.
* **[Cassovary ★ 837 ⧗ 1](https://github.com/twitter/cassovary)** - A Scala library that is designed from the ground up for space efficiency, handling graphs with billions of nodes and edges.
* [cats ★ 3 ⧗ 9](https://github.com/non/cats) - Lightweight, modular, and extensible library for functional programming.
* [Each ★ 94 ⧗ 11](https://github.com/ThoughtWorksInc/each) - A macro library that converts native imperative syntax to [Scalaz](https://github.com/scalaz/scalaz)'s monadic expressions.
* [enableIf.scala ★ 26 ⧗ 20](https://github.com/ThoughtWorksInc/enableIf.scala) - A library that switches Scala code at compile-time, like `#if` in C/C++.
* [Enumeratum ★ 178 ⧗ 0](https://github.com/lloydmeta/enumeratum) - A macro to replace Scala enumerations with a sealed family of case objects. This allows additional checks for the compiler, e.g. for missing cases in a match statement. Has additinal support for Json libraries and the Play framework.
* [Hamsters ★ 99 ⧗ 8](https://github.com/scala-hamsters/hamsters) - A mini Scala utility library. Compatible with functional programming beginners. Featuring validation, monad transformers, HLists, Union types.
* [Lamma ★ 57 ⧗ 1](https://github.com/maxcellent/lamma) - A Scala date library for date and schedule generation.
* [Log4s](http://www.log4s.org/) - Fast, Scala-friendly logging bindings on top of [SLF4J](http://slf4j.org/). Uses macros for extreme performance.
* **[Monocle ★ 600 ⧗ 0](https://github.com/julien-truffaut/Monocle)** - An Optics/Lens library for purely functional manipulation of immutable objects.
* [Persist-Logging ★ 21 ⧗ 5](https://github.com/nestorpersist/logging) - Comprehensive logging library for Scala.
* [Quicklens ★ 194 ⧗ 2](https://github.com/adamw/quicklens) - modify deeply nested case class fields with an elegant API
* [Rapture](http://rapture.io/) ([repo](https://github.com/propensive/rapture)) - a collection of libraries for common, everyday programming tasks (I/O, JSON, i18n, etc.)
* [refined ★ 293 ⧗ 2](https://github.com/fthomas/refined) - Simple refinement types with compile- and runtime checking
* [Resolvable ★ 31 ⧗ 63](https://github.com/resolvable/resolvable) - A library to optimize fetching immutable data structures from several endpoints in several formats.
* **[Scala Async ★ 680 ⧗ 8](https://github.com/scala/async)** - An asynchronous programming facility for Scala.
* [Scala Blitz](http://scala-blitz.github.io/) - A library to speed up Scala collection operations by removing runtime overheads during compilation, and a custom data-parallel operation runtime.
* [Scala Graph](http://www.scala-graph.org/) - A Scala library with basic graph functionality that seamlessly fits into the Scala standard collections library.
* [scala.meta](http://scalameta.org/) - A clean-room implementation of a metaprogramming toolkit for Scala.
* [Scalactic](http://www.scalactic.org/) - Small library of utilities related to quality that helps keeping code clear and correct.
* **[Scalaz ★ 2649 ⧗ 0](https://github.com/scalaz/scalaz)** - An extension to the core Scala library for functional programming.
* **[Shapeless ★ 1654 ⧗ 0](https://github.com/milessabin/shapeless)** - A type class and dependent type based generic programming library for Scala.
* [Stateless Future ★ 142 ⧗ 6](https://github.com/qifun/stateless-future) - Asynchronous programming in fully featured Scala syntax.
* **[Twitter Util ★ 1593 ⧗ 2](https://github.com/twitter/util)** - General-purpose Scala libraries, including a future implementation and other concurrency tools.

## Misc

*Projects that don't fit into any specific category.*

* [Ammonite-REPL](http://lihaoyi.github.io/Ammonite/#Ammonite-REPL) - An improved Scala REPL: syntax highlighting, output formatting, multi-line input, and more.
* [Fansi ★ 72 ⧗ 5](https://github.com/lihaoyi/fansi) - Scala/Scala.js library for manipulating Fancy Ansi colored strings
* [Miniboxing](https://github.com/miniboxing/miniboxing-plugin)- A Scala compiler plugin that improves program performance -- [see the project web site](http://scala-miniboxing.org) - Less boxes
* [Openquant ★ 73 ⧗ 0](https://github.com/openquant) - A Scala open source quantitative trading platform
* [Play Swagger ★ 103 ⧗ 6](https://github.com/iheartradio/play-swagger) - Automatically create Swagger documentation for your Play REST API
* [REPLesent ★ 272 ⧗ 5](https://github.com/marconilanna/REPLesent) - A presentation tool built inside the Scala REPL. Runs code straight from your slides with a single keystroke.
* [scala-ssh ★ 169 ⧗ 0](https://github.com/sirthias/scala-ssh) - Remote shell access via SSH for your Scala applications
* [Scalan ★ 71 ⧗ 2](https://github.com/scalan/scalan) - A framework for development of domain-specific compilers in Scala
* [ScalaSTM](https://nbronson.github.io/scala-stm/) - Software Transaction Memory for Scala
* [Simple Scala Config ★ 20 ⧗ 0](https://github.com/ElderResearch/ssc) - Thin, idiomatic Scala wrapper around [Typesafe Config](https://github.com/typesafehub/config) with custom `Reader[T]` suppport.
* [YahooFinanceScala ★ 5 ⧗ 0](https://github.com/openquant/YahooFinanceScala) - Get stock data from Yahoo Finance using Akka http.
* [GoogleApiScala](https://github.com/EckerdCollege/google-api-scala) - A simple scala library offering control of Google Drive, Calendar, and the Admin SDK.

## Android

*Scala libraries and wrappers for Android development.*

* [Android SDK Plugin for SBT ★ 491 ⧗ 0](https://github.com/pfn/android-sdk-plugin) - An sbt plugin that adds tasks for developing Android applications.
* [Gradle Android Scala Plugin ★ 287 ⧗ 8](https://github.com/saturday06/gradle-android-scala-plugin) - A gradle plugin that allows you to use Scala with Android
* [Macroid ★ 443 ⧗ 7](https://github.com/47deg/macroid) - A modular functional UI language for Android.
* **[Scaloid ★ 1990 ⧗ 0](https://github.com/pocorall/scaloid)** - Less painful Android development with Scala.

## HTTP

*Scala libraries and wrappers for HTTP clients.*

* [Dispatch ★ 346 ⧗ 1](https://github.com/dispatch/reboot) - Library for asynchronous HTTP interaction. It provides a Scala vocabulary for Java’s [async-http-client](https://github.com/AsyncHttpClient/async-http-client).
* **[Finch.io ★ 743 ⧗ 0](https://github.com/finagle/finch)** - Purely Functional REST API atop of [Finagle](https://github.com/twitter/finagle).
* **[Http4s ★ 517 ⧗ 0](https://github.com/http4s/http4s)** - A minimal, idiomatic Scala interface for HTTP.
* [Netcaty ★ 11 ⧗ 178](https://github.com/ngocdaothanh/netcaty) - Simple net test client/server for Netty and Scala lovers.
* [Newman ★ 239 ⧗ 41](https://github.com/stackmob/newman) - A REST DSL that tries to take the best from Dispatch, Finagle and Apache HttpClient. See [here](https://www.paypal-engineering.com/2014/02/13/hello-newman-a-rest-client-for-scala/) for rationale.
* [scalaj-http ★ 436 ⧗ 0](https://github.com/scalaj/scalaj-http) - Simple scala wrapper for HttpURLConnection (including OAuth support).
* [Scalaxb ★ 204 ⧗ 9](https://github.com/eed3si9n/scalaxb) - An XML data-binding tool for Scala that supports W3C XML Schema (xsd) and Web Services Description Language (wsdl) as the input file.
* [Spray](http://spray.io/) - Actor-based library for http interaction.
* [Tubesocks ★ 7 ⧗ 253](https://github.com/softprops/tubesocks) - Library supporting bi-directional communication with websocket servers.

## Semantic Web

*Scala libraries for interactions with the Web of Data, and other RDF tools.*

* [Banana-RDF ★ 185 ⧗ 10](https://github.com/banana-rdf/banana-rdf) - Scala-friendly abstractions for RDF and Linked Data technologies. Supports Jena, Sesame and native Scala.
* [rdfp ★ 1 ⧗ 337](https://github.com/jannvck/rdfp) - RDF stream processing framework in Scala

## Metrics and Monitoring

*Scala libraries for gathering metrics and monitoring applications.*

* [Kamon](http://kamon.io) - Gathering metrics from applications built with Akka, Spray and Play! with support for user metrics as well.

## Parsing

*Scala libraries for creating parsers.*

* [atto ★ 121 ⧗ 31](https://github.com/tpolecat/atto) - Pure functional incremental text parsing library for Scala, based on Attoparsec.
* [Fast Parse ★ 380 ⧗ 2](https://github.com/lihaoyi/fastparse) - Fast to write, Fast running Parsers in Scala
* [Parboiled2 ★ 451 ⧗ 4](https://github.com/sirthias/parboiled2) - A Fast Parser Generator for Scala 2.10.3+.
* [Scala Parser Combinators ★ 159 ⧗ 5](https://github.com/scala/scala-parser-combinators) - Scala Standard Parser Combinator Library.

## Sbt plugins

*Sbt plugins to make your life easier.*

* [pttrt ★ 3 ⧗ 37](https://github.com/Atry/pttrt) - A sbt plugin, designed to pass data from compile-time to run-time.
* [sbt-api-mappings ★ 30 ⧗ 38](https://github.com/ThoughtWorksInc/sbt-api-mappings) - A Sbt plugin that resolves external API links to common Scala libraries.
* [sbt-buildinfo ★ 222 ⧗ 2](https://github.com/sbt/sbt-buildinfo) - Generates Scala source from build definition.
* [sbt-classfinder ★ 3 ⧗ 70](https://github.com/ruippeixotog/sbt-classfinder) - Retrieves runtime information about the classes and traits in a project.
* [sbt-cppp ★ 4 ⧗ 6](https://github.com/Atry/sbt-cppp) - A sbt plugin to support [Protocol Buffers](https://github.com/google/protobuf), especially in multi-project builds.
* **[sbt-dependency-graph ★ 580 ⧗ 0](https://github.com/jrudolph/sbt-dependency-graph)** - Create a dependency graph for your project.
* [sbt-groll ★ 80 ⧗ 9](https://github.com/sbt/sbt-groll) - sbt plugin to roll the Git history.
* [sbt-haxe ★ 9 ⧗ 7](https://github.com/qifun/sbt-haxe) - A Sbt plugin to compile Haxe sources.
* [sbt-ide-settings ★ 24 ⧗ 70](https://github.com/Jetbrains/sbt-ide-settings) - SBT plugin for tweaking various IDE settings
* **[sbt-native-packager ★ 650 ⧗ 0](https://github.com/sbt/sbt-native-packager)** - Bundle up Scala software for native packaging systems, like deb, rpm, homebrew, msi..
* [sbt-pack ★ 256 ⧗ 19](https://github.com/xerial/sbt-pack) - A sbt plugin for creating distributable Scala packages.
* [sbt-revolver ★ 448 ⧗ 1](https://github.com/spray/sbt-revolver) - Fork & Stop processes from sbt.
* [sbt-robovm ★ 106 ⧗ 26](https://github.com/roboscala/sbt-robovm) - An sbt plugin for iOS development in Scala
* [sbt-scala-js-map ★ 9 ⧗ 70](https://github.com/ThoughtWorksInc/sbt-scala-js-map) - A sbt plugin that configures source mapping for Scala.js projects hosted on Github
* [sbt-sublime ★ 134 ⧗ 7](https://github.com/orrsella/sbt-sublime) - Create Sublime Text projects with library dependencies sources
* [sbt-updates ★ 260 ⧗ 2](https://github.com/rtimush/sbt-updates) - Shows sbt project's dependency updates.
* [sbt-versions ★ 11 ⧗ 23](https://github.com/sksamuel/sbt-versions) - Plugin that checks for updated versions of your project's dependencies.
* [sbt-view ★ 5 ⧗ 106](https://github.com/nestorpersist/sbt-view) - View ScalaDoc/JavaDoc in browser window.
* **[sbteclipse ★ 581 ⧗ 1](https://github.com/typesafehub/sbteclipse)** - Create Eclipse project definitions from sbt builds.
* [ScalaKata2 ★ 55 ⧗ 0](https://github.com/MasseGuillaume/ScalaKata2) - Scala playground & Documentation tool.
* [tut ★ 261 ⧗ 6](https://github.com/tpolecat/tut) - Tool for writing documentation with typechecked examples.
* [xsbt-web-plugin ★ 315 ⧗ 15](https://github.com/earldouglas/xsbt-web-plugin) - Build enterprise J2EE Web applications in Scala.
* [coursier](https://github.com/alexarchambault/coursier) - A Scala library to fetch dependencies from Maven / Ivy repositories

## XML / HTML

*XML and HTML generation and processing*

* [scala-scraper ★ 187 ⧗ 5](https://github.com/ruippeixotog/scala-scraper) - A library for scraping content from HTML pages.
* [Scalatags ★ 407 ⧗ 0](https://github.com/lihaoyi/scalatags) - Write html as scala code and have your ide syntax check it.
* [xs4s ★ 23 ⧗ 7](https://github.com/ScalaWilliam/xs4s) - XML Streaming for Scala for processing large (gigabytes and over) XML files.

## Learning Scala

*Nice books, blogs and other resources to learn Scala*

* [Demos and Examples in Scala (Chinese) ★ 342 ⧗ 0](https://github.com/jacksu/utils4s) - repo of sample Scala library usage, written in Chinese
* [Deploying Scala libraries to Sonatype for dummies ★ 18 ⧗ 23](https://github.com/larroy/deployingScalaLibrariesToSonatype) - None
* [Functional Programming in Scala](https://www.coursera.org/specializations/scala) - Coursera Specialization (4 courses) created by  Martin Odersky et al. at the EPFL (Ecole polytechnique fédérale de Lausanne).
* [Reactive Programming with Scala and Akka](http://www.foxebook.net/reactive-programming-with-scala-and-akka/) - Use the concepts of reactive programming to build distributed systems running on multiple nodes
* [Scala Exercises](http://scala-exercises.47deg.com/) - Brings the popular Scala Koans to the web. Offering hundreds of solvable exercises organized into 42 categories covering the basics of the Scala language.
* [Scala in Depth](https://www.manning.com/books/scala-in-depth) - None
* [Scala school](https://twitter.github.io/scala_school/) - Scala school started as a series of lectures at Twitter to prepare experienced engineers to be productive Scala programmers.
* [Scalera Blog](http://www.scalera.es) - Blog about Scala language and its environment (howto's, good practices, tips,...). Weekly posts written in both spanish and english
* [The Neophyte's Guide to Scala](http://danielwestheide.com/scala/neophytes.html) - None

## JavaScript

*JavaScript generation and interop libraries.*

* [js-scala ★ 151 ⧗ 81](https://github.com/js-scala/js-scala) - JavaScript as an embedded DSL in Scala
* [scala-js-fiddle](http://www.scala-js-fiddle.com/) ([repo](https://github.com/lihaoyi/scala-js-fiddle)) - Browser-based Scala.js playground
* [Scala.js](http://www.scala-js.org/) ([repo](https://github.com/scala-js/scala-js)) - Scala to JavaScript compiler

## Tools

* [Abide ★ 220 ⧗ 1](https://github.com/scala/scala-abide) - Library for quick scala code checking and validation
* [Codacy](https://www.codacy.com/) - Automated Code Reviews for Scala
* [Fastring ★ 75 ⧗ 2](https://github.com/Atry/fastring) - Extremely fast string formatting
* **[Gitbucket ★ 5831 ⧗ 0](https://github.com/gitbucket/gitbucket)** - The easily installable GitHub clone powered by Scala
* [sbt](http://www.scala-sbt.org/) ([repo](https://github.com/sbt/sbt)) - The interactive build tool for Scala
* [Scala @LibHunt](https://scala.libhunt.com) - The go-to Scala Toolbox.
* [scala-trace-debug ★ 55 ⧗ 9](https://github.com/JohnReedLOL/scala-trace-debug) - Multithreaded print debug tool
* [Scalariform ★ 121 ⧗ 77](https://github.com/daniel-trinh/scalariform) - Scala source code formatter
* [Scalastyle ★ 394 ⧗ 0](https://github.com/scalastyle/scalastyle) - Scala style checker.
* [Scalatex ★ 204 ⧗ 0](https://github.com/lihaoyi/Scalatex) - Programmable, Typesafe Document Generation
* [Scapegoat ★ 146 ⧗ 6](https://github.com/sksamuel/scapegoat) - Scala compiler plugin for static code analysis
* [Scaps](http://scala-search.org/) ([repo](https://github.com/scala-search/scaps)) - A search engine for Scala libraries
* [Scoverage](https://github.com/scoverage) - Scala Code Coverage tool
* **[Wartremover ★ 532 ⧗ 1](https://github.com/puffnfresh/wartremover)** - Wartremover a flexible Scala code linting tool

# Contributing

Your contributions are always welcome! Please submit a pull request or create an issue to add a new framework, library or software to the list. Do not submit a project that hasn’t been updated in the past 6 months or is not awesome.
