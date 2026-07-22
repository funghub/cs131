from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml import Pipeline,PipelineModel
from pyspark.ml.evaluation import RegressionEvaluator
import sys

# arguments passed in from the command line
input_path  = sys.argv[1]

# A1
spark = SparkSession.builder.appName("ws5-regression").getOrCreate()

# A2
df = spark.read.csv(input_path, header=True, inferSchema=True)
df.show(5)            # first 5 rows

# A3
vecAssembler = VectorAssembler(inputCols=["total_bill","size"],outputCol="features")

# A4
trainDF, testDF = df.randomSplit([.8,.2], seed=42)
#vecTrainDF = vecAssembler.transform(trainDF) # not sure if this should be here
#vecTrainDF.show(10)

# A5
lr = LinearRegression(featuresCol="features",labelCol="tip")
# lrModel = lr.fit(vectorTrainDF)

pipeline = Pipeline(stages=[vecAssembler, lr])
pipelineModel = pipeline.fit(trainDF)

# A6
predDF = pipelineModel.transform(testDF)
predDF.show(10)

# A7
regressionEvaluator_rmse = RegressionEvaluator(
        predictionCol = "prediction",
        labelCol = "tip",
        metricName = "rmse")
rmse = regressionEvaluator_rmse.evaluate(predDF)

regressionEvaluator_r2 = RegressionEvaluator(
        predictionCol = "prediction",
        labelCol = "tip",
        metricName = "r2")
r2_score = regressionEvaluator_r2.evaluate(predDF)

# A8
lr_pipelinemodel = pipelineModel.stages[-1]

print(f"Coefficients: {lr_pipelinemodel.coefficients}")
print(f"Intercept: {lr_pipelinemodel.intercept}\n")

print(f"RMSE: {rmse}")
print(f"R2: {r2_score}")
