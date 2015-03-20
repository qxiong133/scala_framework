
cd ..
sbt -J-Xss1m -J-Xms256m -J-Xmx512m -J-XX:+CMSClassUnloadingEnabled package && ~/spark-1.2.0-bin-hadoop2.4/bin/spark-submit --class "SimpleApp" --master local[4] target/scala-2.10/simple-project_2.10-1.0.jar localhost 9999
