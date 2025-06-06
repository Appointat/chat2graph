export const defaultLanguage = 'en-us';

export const languages = [
  { code: 'en-us', name: 'English' },
  { code: 'zh-cn', name: '中文' },
] as const;

export type Language = typeof languages[number]['code'];

export const isValidLanguage = (lang: string): lang is Language => {
  return languages.some(l => l.code === lang);
};

export const getLanguageFromPath = (pathname: string): Language => {
  const segments = pathname.split('/').filter(Boolean);
  
  // 检查是否是文档路径格式：/chat2graph/[lang]/...
  if (segments.length >= 2 && segments[0] === 'chat2graph') {
    const langSegment = segments[1];
    if (isValidLanguage(langSegment)) {
      return langSegment;
    }
  }
  
  // 检查第一个段是否是语言代码（用于其他路径格式）
  const firstSegment = segments[0];
  if (isValidLanguage(firstSegment)) {
    return firstSegment;
  }
  
  return defaultLanguage;
};

export const removeLanguageFromPath = (pathname: string): string => {
  const segments = pathname.split('/').filter(Boolean);
  const firstSegment = segments[0];
  
  if (isValidLanguage(firstSegment)) {
    return '/' + segments.slice(1).join('/');
  }
  
  return pathname;
};

export const addLanguageToPath = (pathname: string, language: Language): string => {
  const cleanPath = removeLanguageFromPath(pathname);
  return `/${language}${cleanPath}`;
};
