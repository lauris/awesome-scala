Awesome Scala
=============

A curated list of awesome Scala frameworks, libraries and software. Inspired by [awesome-python](https://github.com/vinta/awesome-python).

- [Awesome Scala](#awesome-scala)
    - [Database](#database)
    - [Web Frameworks](#web-frameworks)
    - [Authentication](#authentication)
    - [Testing](#testing)
    - [JSON Manipulation](#json-manipulation)
    - [Science and Data Analysis](#science-and-data-analysis)
    - [Big Data](#big-data)
    - [Modularization and Dependency Injection](#modularization-and-dependency-injection)
    - [Extensions](#extensions)
    - [Android](#android)
    - [HTTP](#http)
- [Contributing](#contributing)

## Database

*Database access libraries in Scala.*

* [ScalikeJDBC](https://github.com/scalikejdbc/scalikejdbc) - A tidy SQL-based DB access library for Scala developers.
* [Slick](https://github.com/slick/slick) - Modern database query and access library for Scala.
* [Squeryl](https://github.com/squeryl/squeryl) - A Scala DSL for talking with databases with minimum verbosity and maximum type safety.
* [Activate](https://github.com/fwbrasil/activate) - Pluggable object persistence in Scala.
* [Scala ActiveRecord](https://github.com/aselab/scala-activerecord) - ORM library for scala, inspired by ActiveRecord of Ruby on Rails.
* [PostgreSQL and MySQL async](https://github.com/mauricio/postgresql-async) - async database drivers to talk to PostgreSQL and MySQL in Scala.

## Web Frameworks

*Scala frameworks for web development.*

* [Play](https://github.com/playframework/playframework) - Makes it easy to build scalable, fast and real-time web applications with Java & Scala.
* [Skinny Framework](https://github.com/skinny-framework/skinny-framework) - A full-stack web app framework upon Scalatra for rapid Development in Scala.
* [Scalatra](https://github.com/scalatra/scalatra) - Tiny Scala high-performance, async web framework, inspired by Sinatra.
* [Spray](https://github.com/spray/spray) - A suite of scala libraries for building and consuming RESTful web services on top of Akka.
* [Finatra](https://github.com/twitter/finatra) - A sinatra-inspired web framework for scala, running on top of Finagle.
* [Blue Eyes](https://github.com/jdegoes/blueeyes) - A lightweight Web 3.0 framework for Scala, featuring a purely asynchronous architecture, extremely high-performance, massive scalability, high usability, and a functional, composable design.
* [Reactive](https://github.com/nafg/reactive) - FRP and web abstractions, which can be plugged into any web framework (currently only has bindings for Lift)
* [Chaos](https://github.com/mesosphere/chaos) - A lightweight framework for writing REST services in Scala

## Authentication

*Libraries for implementing authentications schemes.*

* [scala-oauth2-provider](https://github.com/nulab/scala-oauth2-provider) - OAuth 2.0 server-side implementation written in Scala.
* [SecureSocial](https://github.com/jaliss/securesocial) - A module that provides OAuth, OAuth2 and OpenID authentication for Play Framework applications.
* [play2-auth](https://github.com/t2v/play2-auth) - Play2.x Authentication and Authorization module.

## Testing

*Libraries for code testing.*

* [ScalaCheck](https://github.com/rickynils/scalacheck) - Property-based testing for Scala.
* [ScalaTest](https://github.com/scalatest/scalatest) - A testing tool for Scala and Java developers.
* [Specs2](https://github.com/etorreborre/specs2) - Software Specifications for Scala.

## JSON Manipulation

*Libraries for work with json.*

* [json4s](https://github.com/json4s/json4s) - project aims to provide a single AST to be used by other scala json libraries.
* [jerkson](https://github.com/codahale/jerkson) - a Scala wrapper for Jackson
* [spray-json](https://github.com/spray/spray-json) -  lightweight, clean and efficient JSON implementation in Scala.
* [argonaut](http://argonaut.io/) - Purely Functional JSON in Scala.
* [jackson-module-scala](https://github.com/FasterXML/jackson-module-scala) - Add-on module for Jackson to support Scala-specific datatypes

## Science and Data Analysis

*Libraries for scientific computing, data analysis and numerical processing.*

* [Breeze](https://github.com/scalanlp/breeze) - Breeze is a numerical processing library for Scala.
* [MLLib](https://spark.apache.org/mllib/) - Machine Learning framework for Spark
* [Spire](https://github.com/non/spire) - Powerful new number types and numeric abstractions for Scala.
* [Algebird](https://github.com/twitter/algebird) - Abstract Algebra for Scala.
* [FACTORIE](https://github.com/factorie/factorie) - A toolkit for deployable probabilistic modeling, implemented as a software library in Scala.
* [scala_prob](https://github.com/urso/scala_prob) - Scala embedded probabilistic programing library using delimited continuations (VERY Experimental).
* [probability-monad](https://github.com/jliszka/probability-monad) - Probability Distribution Monad in Scala.
* [Saddle](https://github.com/saddle/saddle) - A minimalist port of Pandas to Scala


## Big Data
* [Spark](http://spark.apache.org/) - Lightning fast cluster computing - up to 100x faster than Hadoop for iterative algorithms (memory caching) and up to 10x faster than Hadoop for single-pass MapReduce jobs. Compatible with YARN-enabled Hadoop clusters, can run on Mesos and in stand-alone mode as well.
* [Scalding](https://github.com/twitter/scalding) - A Scala binding for the Cascading abstraction of Hadoop MapReduce.
* [Summingbird](https://github.com/twitter/summingbird) - An implementation of the "lambda architecture" as a software abstraction - a single API for Hadoop and Storm.
* [Scrunch](http://crunch.apache.org/scrunch.html) - A Scala wrapper for [Apache Crunch](http://crunch.apache.org/index.html) which provides a framework for writing, testing, and running MapReduce pipelines.

## Modularization and Dependency Injection

*Modularization of applications, dependency injection, etc.*

* [Domino](https://github.com/helgoboss/domino) - Write elegant OSGi bundle activators in Scala.
* [Scaldi](https://github.com/scaldi/scaldi) - Lightweight Scala Dependency Injection Library.
* [MacWire](https://github.com/adamw/macwire) - Scala Macro to generate wiring code for class instantiation. DI container replacement.
* [SubCut](https://github.com/dickwall/subcut) - Scala Uniquely Bound Classes Under Traits.

## Extensions

*Scala extensions.*

* [Scalaz](https://github.com/scalaz/scalaz) - An extension to the core Scala library for functional programming.
* [Shapeless](https://github.com/milessabin/shapeless) - A type class and dependent type based generic programming library for Scala.

## Android

*Scala libraries and wrappers for Android development.*

* [Scaloid](https://github.com/pocorall/scaloid) - Less painful Android development with Scala.
* [Macroid](https://github.com/macroid/macroid) - A modular functional UI language for Android.
* [Android SDK Plugin for SBT](https://github.com/pfn/android-sdk-plugin) - A sbt plugin that adds tasks for developing Android applications.

## HTTP

*Scala libraries and wrappers for HTTP clients.*

* [Dispatch](https://github.com/dispatch/reboot) - Library for asynchronous HTTP interaction. It provides a Scala vocabulary for Java’s [async-http-client](https://github.com/AsyncHttpClient/async-http-client).
* [Scalaxb](https://github.com/eed3si9n/scalaxb) - An XML data-binding tool for Scala that supports W3C XML Schema (xsd) and Web Services Description Language (wsdl) as the input file.
* [Spray](http://spray.io/) - Actors-based library for http interaction.


# Contributing

Your contributions are always welcome! Please submit a pull request or create an issue to add a new framework, library or software to the list.
