# Databricks notebook source
5 + 6

# COMMAND ----------

getOption("repos")


# COMMAND ----------

local({
  options(repos = c("CRAN" = "https://fkl1uo9d3h-nxrm.sonatype-se.com/repository/r-group/"))
})

# COMMAND ----------

getOption("repos")

# COMMAND ----------

#install.packages("tidyverse", repos = "https://288fec91b6b6.ngrok.app/repository/r-group/")
install.packages("tidyverse")


# COMMAND ----------

#The tidyverse is an opinionated collection of R packages designed for data science
library(tidyverse)

# COMMAND ----------

glimpse(starwars)

# COMMAND ----------

starwars %>% 
  filter (height > 150 & mass < 200) %>% 
  mutate(height_in_m = height / 100) %>% 
  select(height_in_m, mass) %>% 
  arrange(mass) %>% 
  #view()
  plot()

# COMMAND ----------

install.packages("gapminder")
library(gapminder)

# COMMAND ----------

glimpse(gapminder)


# COMMAND ----------

data <- select(gapminder, country, year, lifeExp)
wider_data <- data %>% 
  pivot_wider(names_from = year, values_from = lifeExp)


# COMMAND ----------

glimpse(wider_data)

# COMMAND ----------

gapminder %>% 
  filter(continent %in% c('Europe', 'Africa')) %>% 
  t.test(lifeExp ~ continent, data = ., 
         altrnative = "two.sided", 
         paired = FALSE)


# COMMAND ----------

#install specific version of readxl which is vulnerable, requires security high policy to fail
packageurl <- "https://fkl1uo9d3h-nxrm.sonatype-se.com/repository/r-group/src/contrib/Archive/readxl/readxl_0.1.0.tar.gz"
install.packages(packageurl, repos=NULL, type="source")

# COMMAND ----------

#install specific version of readxl which is OK, not vulnerable will not fail
packageurl <- "https://fkl1uo9d3h-nxrm.sonatype-se.com/repository/r-group/src/contrib/Archive/readxl/readxl_1.4.1.tar.gz"
install.packages(packageurl, repos=NULL, type="source")

# COMMAND ----------

getOption("repos")


# COMMAND ----------

#Update CRAN Repo
local({
  options(repos = c("CRAN" = "https://fkl1uo9d3h-nxrm.sonatype-se.com/repository/r-group/"))
})

# COMMAND ----------

install.packages("devtools")

# COMMAND ----------

r = getOption("repos") 
r["CRAN"] = "https://fkl1uo9d3h-nxrm.sonatype-se.com/repository/r-group/"
options(repos = r)
rm(r)

# COMMAND ----------

options(repos = "https://fkl1uo9d3h-nxrm.sonatype-se.com/repository/r-group/")

# COMMAND ----------

install.packages("gapminder")

# COMMAND ----------

getOption("repos") 


# COMMAND ----------

#install widgetfram, current version not vulnerable, older versions are
install.packages("widgetframe")
#0.2.0 vulnerable


# COMMAND ----------

#Firewall should block this as all versions are vulnerable, requires security medium policy
install.packages("xgboost")

# COMMAND ----------

#this provides the capability for install_version function
install.packages("remotes")
library(remotes)
  


# COMMAND ----------

#vulnerable version
install_version("widgetframe", "0.2.0")

# COMMAND ----------

getOption("repos")


# COMMAND ----------

install.packages("tidyverse", repos = "https://288fec91b6b6.ngrok.app/repository/r-group/")

# COMMAND ----------


