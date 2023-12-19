# Databricks notebook source
# MAGIC %r
# MAGIC 5 + 6

# COMMAND ----------

# MAGIC %r
# MAGIC getOption("repos")
# MAGIC

# COMMAND ----------

# MAGIC %r
# MAGIC local({
# MAGIC   options(repos = c("CRAN" = "https://fkl1uo9d3h-nxrm.sonatype-se.com/repository/r-group/"))
# MAGIC })

# COMMAND ----------

# MAGIC %r
# MAGIC getOption("repos")

# COMMAND ----------

# MAGIC %r
# MAGIC #install.packages("tidyverse", repos = "https://288fec91b6b6.ngrok.app/repository/r-group/")
# MAGIC install.packages("tidyverse")
# MAGIC

# COMMAND ----------

# MAGIC %r
# MAGIC #The tidyverse is an opinionated collection of R packages designed for data science
# MAGIC library(tidyverse)

# COMMAND ----------

# MAGIC %r
# MAGIC glimpse(starwars)

# COMMAND ----------

# MAGIC %r
# MAGIC starwars %>% 
# MAGIC   filter (height > 150 & mass < 200) %>% 
# MAGIC   mutate(height_in_m = height / 100) %>% 
# MAGIC   select(height_in_m, mass) %>% 
# MAGIC   arrange(mass) %>% 
# MAGIC   #view()
# MAGIC   plot()

# COMMAND ----------

# MAGIC %r
# MAGIC install.packages("gapminder")
# MAGIC library(gapminder)

# COMMAND ----------

# MAGIC %r
# MAGIC glimpse(gapminder)
# MAGIC

# COMMAND ----------

# MAGIC %r
# MAGIC data <- select(gapminder, country, year, lifeExp)
# MAGIC wider_data <- data %>% 
# MAGIC   pivot_wider(names_from = year, values_from = lifeExp)
# MAGIC

# COMMAND ----------

# MAGIC %r
# MAGIC glimpse(wider_data)

# COMMAND ----------

# MAGIC %r
# MAGIC gapminder %>% 
# MAGIC   filter(continent %in% c('Europe', 'Africa')) %>% 
# MAGIC   t.test(lifeExp ~ continent, data = ., 
# MAGIC          altrnative = "two.sided", 
# MAGIC          paired = FALSE)
# MAGIC

# COMMAND ----------

# MAGIC %r
# MAGIC #install specific version of readxl which is vulnerable, requires security high policy to fail
# MAGIC packageurl <- "https://fkl1uo9d3h-nxrm.sonatype-se.com/repository/r-group/src/contrib/Archive/readxl/readxl_0.1.0.tar.gz"
# MAGIC install.packages(packageurl, repos=NULL, type="source")

# COMMAND ----------

# MAGIC %r
# MAGIC #install specific version of readxl which is OK, not vulnerable will not fail
# MAGIC packageurl <- "https://fkl1uo9d3h-nxrm.sonatype-se.com/repository/r-group/src/contrib/Archive/readxl/readxl_1.4.1.tar.gz"
# MAGIC install.packages(packageurl, repos=NULL, type="source")

# COMMAND ----------

# MAGIC %r
# MAGIC getOption("repos")
# MAGIC

# COMMAND ----------

# MAGIC %r
# MAGIC #Update CRAN Repo
# MAGIC local({
# MAGIC   options(repos = c("CRAN" = "https://fkl1uo9d3h-nxrm.sonatype-se.com/repository/r-group/"))
# MAGIC })

# COMMAND ----------

# MAGIC %r
# MAGIC install.packages("devtools")

# COMMAND ----------

# MAGIC %r
# MAGIC r = getOption("repos") 
# MAGIC r["CRAN"] = "https://fkl1uo9d3h-nxrm.sonatype-se.com/repository/r-group/"
# MAGIC options(repos = r)
# MAGIC rm(r)

# COMMAND ----------

# MAGIC %r
# MAGIC options(repos = "https://fkl1uo9d3h-nxrm.sonatype-se.com/repository/r-group/")

# COMMAND ----------

# MAGIC %r
# MAGIC install.packages("gapminder")

# COMMAND ----------

# MAGIC %r
# MAGIC getOption("repos") 
# MAGIC

# COMMAND ----------

# MAGIC %r
# MAGIC #install widgetfram, current version not vulnerable, older versions are
# MAGIC install.packages("widgetframe")
# MAGIC #0.2.0 vulnerable
# MAGIC

# COMMAND ----------

# MAGIC %r
# MAGIC #Firewall should block this as all versions are vulnerable, requires security medium policy
# MAGIC install.packages("xgboost")

# COMMAND ----------

# MAGIC %r
# MAGIC #this provides the capability for install_version function
# MAGIC install.packages("remotes")
# MAGIC library(remotes)
# MAGIC   
# MAGIC

# COMMAND ----------

# MAGIC %r
# MAGIC #vulnerable version
# MAGIC install_version("widgetframe", "0.2.0")

# COMMAND ----------

# MAGIC %r
# MAGIC getOption("repos")
# MAGIC

# COMMAND ----------

# MAGIC %r
# MAGIC install.packages("tidyverse", repos = "https://288fec91b6b6.ngrok.app/repository/r-group/")

# COMMAND ----------


