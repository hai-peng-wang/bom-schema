import bom.ProducerProto.Producer;
import bom.TaskProto.TaskEvent;
import bom.ComponentProto.Component;
import bom.ComponentLevelProto.ComponentLevel;
import com.google.protobuf.TextFormat;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.FileOutputStream;
import java.io.IOException;

// import java.io.BufferedReader;
// import java.io.FileInputStream;
// import java.io.FileNotFoundException;
// import java.io.InputStreamReader;
// import java.io.PrintStream;

class TestTaskEvent {
  static Producer appProducer() {
    // This function fills in a Producer message
    Producer.Builder producer = Producer.newBuilder();
    Component.Builder component = Component.newBuilder();
    Component.Info.Builder info = Component.Info.newBuilder();
    component.setInfo(info);
    producer.addComponents(component);

    return producer.build();
  }

  static TaskEvent fromText(String str) throws TextFormat.ParseException {
    TaskEvent.Builder task_event = TaskEvent.newBuilder();
    TextFormat.getParser().merge(str, task_event);
    return task_event.build();
  }

  public static void main(String[] args) throws Exception {
    TaskEvent task_event = null;
    Producer producer = TestTaskEvent.appProducer();

    String str = producer.toString();
    System.out.println(str);

    System.out.println("----------------");
    Path path = Paths.get(args[0]);
    String filestr = new String(Files.readAllBytes(path));
    try {
      task_event = fromText(filestr);
      str = task_event.toString();
      System.out.println(str);
    } catch (TextFormat.ParseException e) {
      e.printStackTrace();
    }
    try {
      // Write the new address book back to disk.
      FileOutputStream output = new FileOutputStream("java_event_msg");
      task_event.writeTo(output);
      output.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
