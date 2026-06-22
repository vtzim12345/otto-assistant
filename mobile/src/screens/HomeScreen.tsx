import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  SafeAreaView,
  ScrollView,
  TouchableOpacity,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';

const HomeScreen = () => {
  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.content}>
        <View style={styles.header}>
          <Text style={styles.greeting}>Welcome to OTTO</Text>
          <Text style={styles.subtitle}>Your Intelligent Personal Assistant</Text>
        </View>

        <View style={styles.orbContainer}>
          <View style={styles.orb}>
            <Text style={styles.orbText}>🎙️</Text>
          </View>
        </View>

        <View style={styles.quickActions}>
          <TouchableOpacity style={styles.actionCard}>
            <Ionicons name="chatbubble-outline" size={32} color="#00D4FF" />
            <Text style={styles.actionTitle}>Chat</Text>
            <Text style={styles.actionDesc}>Start a conversation</Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.actionCard}>
            <Ionicons name="mic-outline" size={32} color="#00D4FF" />
            <Text style={styles.actionTitle}>Voice</Text>
            <Text style={styles.actionDesc}>Speak with OTTO</Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.actionCard}>
            <Ionicons name="image-outline" size={32} color="#00D4FF" />
            <Text style={styles.actionTitle}>Vision</Text>
            <Text style={styles.actionDesc}>Analyze images</Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.actionCard}>
            <Ionicons name="folder-outline" size={32} color="#00D4FF" />
            <Text style={styles.actionTitle}>Projects</Text>
            <Text style={styles.actionDesc}>Organize chats</Text>
          </TouchableOpacity>
        </View>

        <View style={styles.suggestionsContainer}>
          <Text style={styles.suggestionsTitle}>Try asking OTTO:</Text>
          <TouchableOpacity style={styles.suggestionCard}>
            <Text style={styles.suggestionText}>"What's the weather?"</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.suggestionCard}>
            <Text style={styles.suggestionText}>"Create a reminder for me"</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.suggestionCard}>
            <Text style={styles.suggestionText}>"Generate an image"</Text>
          </TouchableOpacity>
        </View>

        <View style={styles.footer}>
          <Text style={styles.footerText}>Created by Victor G.</Text>
          <Text style={styles.footerEmail}>suporte.dev.victor@gmail.com</Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0F172A',
  },
  content: {
    padding: 16,
    paddingBottom: 32,
  },
  header: {
    marginBottom: 32,
    alignItems: 'center',
  },
  greeting: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 14,
    color: '#999',
  },
  orbContainer: {
    alignItems: 'center',
    marginBottom: 32,
  },
  orb: {
    width: 120,
    height: 120,
    borderRadius: 60,
    backgroundColor: '#1E293B',
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 2,
    borderColor: '#00D4FF',
  },
  orbText: {
    fontSize: 60,
  },
  quickActions: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    marginBottom: 32,
  },
  actionCard: {
    width: '48%',
    backgroundColor: '#1E293B',
    borderRadius: 16,
    padding: 16,
    marginBottom: 12,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#334155',
  },
  actionTitle: {
    fontSize: 14,
    fontWeight: '600',
    color: '#fff',
    marginTop: 8,
  },
  actionDesc: {
    fontSize: 12,
    color: '#999',
    marginTop: 4,
    textAlign: 'center',
  },
  suggestionsContainer: {
    marginBottom: 32,
  },
  suggestionsTitle: {
    fontSize: 16,
    fontWeight: '600',
    color: '#fff',
    marginBottom: 12,
  },
  suggestionCard: {
    backgroundColor: '#1E293B',
    borderRadius: 12,
    paddingHorizontal: 12,
    paddingVertical: 10,
    marginBottom: 8,
    borderWidth: 1,
    borderColor: '#334155',
  },
  suggestionText: {
    color: '#00D4FF',
    fontSize: 13,
  },
  footer: {
    alignItems: 'center',
    paddingTop: 16,
    borderTopWidth: 1,
    borderTopColor: '#334155',
  },
  footerText: {
    color: '#999',
    fontSize: 12,
  },
  footerEmail: {
    color: '#00D4FF',
    fontSize: 11,
    marginTop: 4,
  },
});

export default HomeScreen;
