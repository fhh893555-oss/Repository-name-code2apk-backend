import 'package:flutter/material.dart';

void main() {
  runApp(const Code2APKApp());
}

class Code2APKApp extends StatelessWidget {
  const Code2APKApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Code2APK App',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.blue,
        ),
        useMaterial3: true,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: const Text('My First App'),
        ),
        body: const Center(
          child: Text(
            'Hello from Code2APK Cloud!',
            style: TextStyle(fontSize: 22),
          ),
        ),
      ),
    );
  }
}
