import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  SafeAreaView,
  ScrollView,
  TouchableOpacity,
  Switch,
  FlatList,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';

const SettingsScreen = () => {
  const [theme, setTheme] = useState('dark');
  const [notifications, setNotifications] = useState(true);
  const [language, setLanguage] = useState('pt-BR');
  const [wakeWord, setWakeWord] = useState('Otto');

  const voices = [
    { id: 'male_br', name: 'João', lang: 'Portuguese' },
    { id: 'female_br', name: 'Maria', lang: 'Portuguese' },
    { id: 'male_en', name: 'John', lang: 'English' },
    { id: 'female_en', name: 'Emma', lang: 'English' },
  ];

  const languages = [
    { id: 'pt-BR', name: 'Portuguese (BR)' },
    { id: 'en-US', name: 'English (US)' },
    { id: 'es-ES', name: 'Spanish' },
  ];

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.content}>
        <Text style={styles.title}>Settings</Text>

        {/* General Section */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>General</Text>

          <View style={styles.settingItem}>
            <View style={styles.settingInfo}>
              <Ionicons name="moon" size={20} color="#00D4FF" />
              <Text style={styles.settingLabel}>Theme</Text>
            </View>
            <Text style={styles.settingValue}>Dark Mode</Text>
          </View>

          <View style={styles.settingItem}>
            <View style={styles.settingInfo}>
              <Ionicons name="language" size={20} color="#00D4FF" />
              <Text style={styles.settingLabel}>Language</Text>
            </View>
            <Text style={styles.settingValue}>{language}</Text>
          </View>
        </View>

        {/* Voice Section */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Voice Settings</Text>

          <View style={styles.settingItem}>
            <View style={styles.settingInfo}>
              <Ionicons name="mic" size={20} color="#00D4FF" />
              <Text style={styles.settingLabel}>Wake Word</Text>
            </View>
            <Text style={styles.settingValue}>{wakeWord}</Text>
          </View>

          <View style={styles.settingItem}>
            <View style={styles.settingInfo}>
              <Ionicons name="volume-high" size={20} color="#00D4FF" />
              <Text style={styles.settingLabel}>Voice Selection</Text>
            </View>
            <Text style={styles.settingValue}>Listen & Choose</Text>
          </View>

          <Text style={styles.voicesSubtitle}>Available Voices</Text>
          {voices.map((voice) => (
            <TouchableOpacity key={voice.id} style={styles.voiceCard}>
              <Text style={styles.voiceName}>{voice.name}</Text>
              <Text style={styles.voiceLang}>{voice.lang}</Text>
            </TouchableOpacity>
          ))}
        </View>

        {/* Notifications Section */}
        <View style={styles.section}>
          <View style={styles.settingItem}>
            <View style={styles.settingInfo}>
              <Ionicons name="notifications" size={20} color="#00D4FF" />
              <Text style={styles.settingLabel}>Notifications</Text>
            </View>
            <Switch
              value={notifications}
              onValueChange={setNotifications}
              trackColor={{ false: '#334155', true: '#00D4FF' }}
              thumbColor={notifications ? '#00D4FF' : '#999'}
            />
          </View>
        </View>

        {/* APIs Section */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Custom APIs</Text>
          <TouchableOpacity style={styles.apiCard}>
            <View style={styles.apiHeader}>
              <Text style={styles.apiName}>OpenAI</Text>
              <Ionicons name="checkmark-circle" size={20} color="#00FF00" />
            </View>
            <Text style={styles.apiStatus}>Connected</Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.apiCard}>
            <View style={styles.apiHeader}>
              <Text style={styles.apiName}>Groq</Text>
              <Ionicons name="add-circle-outline" size={20} color="#999" />
            </View>
            <Text style={styles.apiStatus}>Add API Key</Text>
          </TouchableOpacity>
        </View>

        {/* Support Section */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Support</Text>
          <TouchableOpacity style={styles.supportItem}>
            <Ionicons name="mail" size={20} color="#00D4FF" />
            <View style={styles.supportInfo}>
              <Text style={styles.supportTitle}>Send Feedback</Text>
              <Text style={styles.supportEmail}>suporte.dev.victor@gmail.com</Text>
            </View>
          </TouchableOpacity>
        </View>

        {/* Footer */}
        <View style={styles.footer}>
          <Text style={styles.footerVersion}>OTTO v1.0.0</Text>
          <Text style={styles.footerCredit}>Created by Victor G.</Text>
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
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 24,
  },
  section: {
    marginBottom: 24,
  },
  sectionTitle: {
    fontSize: 16,
    fontWeight: '600',
    color: '#00D4FF',
    marginBottom: 12,
  },
  settingItem: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: '#1E293B',
    borderRadius: 12,
    paddingHorizontal: 16,
    paddingVertical: 12,
    marginBottom: 8,
    borderWidth: 1,
    borderColor: '#334155',
  },
  settingInfo: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
  },
  settingLabel: {
    fontSize: 14,
    fontWeight: '500',
    color: '#E2E8F0',
  },
  settingValue: {
    fontSize: 12,
    color: '#999',
  },
  voicesSubtitle: {
    fontSize: 12,
    color: '#999',
    marginTop: 12,
    marginBottom: 8,
  },
  voiceCard: {
    backgroundColor: '#1E293B',
    borderRadius: 12,
    paddingHorizontal: 16,
    paddingVertical: 10,
    marginBottom: 8,
    borderWidth: 1,
    borderColor: '#334155',
  },
  voiceName: {
    fontSize: 14,
    fontWeight: '500',
    color: '#00D4FF',
  },
  voiceLang: {
    fontSize: 12,
    color: '#999',
    marginTop: 2,
  },
  apiCard: {
    backgroundColor: '#1E293B',
    borderRadius: 12,
    paddingHorizontal: 16,
    paddingVertical: 12,
    marginBottom: 8,
    borderWidth: 1,
    borderColor: '#334155',
  },
  apiHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  apiName: {
    fontSize: 14,
    fontWeight: '600',
    color: '#E2E8F0',
  },
  apiStatus: {
    fontSize: 12,
    color: '#999',
    marginTop: 4,
  },
  supportItem: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#1E293B',
    borderRadius: 12,
    paddingHorizontal: 16,
    paddingVertical: 12,
    borderWidth: 1,
    borderColor: '#334155',
    gap: 12,
  },
  supportInfo: {
    flex: 1,
  },
  supportTitle: {
    fontSize: 14,
    fontWeight: '500',
    color: '#E2E8F0',
  },
  supportEmail: {
    fontSize: 12,
    color: '#00D4FF',
    marginTop: 2,
  },
  footer: {
    alignItems: 'center',
    paddingTop: 24,
    borderTopWidth: 1,
    borderTopColor: '#334155',
  },
  footerVersion: {
    fontSize: 12,
    color: '#999',
  },
  footerCredit: {
    fontSize: 12,
    color: '#00D4FF',
    marginTop: 4,
  },
});

export default SettingsScreen;
