
sbt package

~/spark-1.2.0-bin-hadoop2.4/bin/spark-submit --class "SimpleApp" --master local[4] target/scala-2.10/simple-project_2.10-1.0.jar