echo "Creating Java and Python builds:"
../protobuf-gradle-plugin/gradlew clean build

echo "Creating html docs:"
rm -rf doc/*
ROOT=$( cd $( dirname $0 ); pwd; )
PATH=$PATH:$ROOT/ext
cd src/proto
protoc --doc_out=html,schema.html:../../doc {./,common/,common/enums/}*.proto
protoc --doc_out=markdown,schema.md:../../doc {./,common/,common/enums/}*.proto
