(function () {
  // 1. MÓDULO — último link do breadcrumb
  const modulo =
    Array.from(document.querySelectorAll('[data-testid="BREADCRUMB_LINK"]')).pop()?.textContent?.trim() ||
    Array.from(document.querySelectorAll('nav .MuiBreadcrumbs-li a')).pop()?.textContent?.trim() ||
    Array.from(document.querySelectorAll('nav li a')).pop()?.textContent?.trim() ||
    'N/A';

  // 2. AULA — item selecionado (aria-selected="true") ou em reprodução
  const selectedLi = document.querySelector('li[aria-selected="true"]');
  const aulaItem = selectedLi || Array.from(document.querySelectorAll('li.MuiListItem-root')).find(li =>
    li.querySelector('.movieStarted.started')
  );
  const aulaTexto =
    aulaItem?.querySelector('.css-om3vjz, .MuiTypography-body1, .MuiListItemText-primary')?.textContent?.trim() ||
    aulaItem?.textContent?.trim()?.replace(/\d{2}:\d{2}(:\d{2})?$/, '').trim() ||
    'N/A';

  // 3. URL
  const pageUrl = window.location.href;

  // 4. RESUMO — parágrafos do bloco h5.css-rymwba ou seção "Resumo da Aula"
  let resumoEl = document.querySelector('h5.css-rymwba');
  if (!resumoEl) {
    const heading = Array.from(document.querySelectorAll('h1,h2,h3,h4,h5,h6')).find(h =>
      /resumo da aula/i.test(h.textContent || '')
    );
    if (heading && heading.parentElement) {
      resumoEl = heading.parentElement;
    }
  }
  const resumo = resumoEl
    ? Array.from(resumoEl.querySelectorAll('p'))
      .map(p => p.textContent.trim())
      .filter(Boolean)
      .join('\n\n')
    : '';

  // 5. TRANSCRIÇÃO — spans de timestamp (formato MM:SS ou HH:MM:SS) independente da classe CSS do Emotion
  const timestampSpans = Array.from(document.querySelectorAll('span')).filter(s =>
    s.children.length === 0 &&
    /^\d{2}:\d{2}(:\d{2})?$/.test(s.textContent.trim()) &&
    s.parentElement &&
    s.parentElement.textContent.trim().length > s.textContent.trim().length + 2
  );
  const transcricao = timestampSpans
    .map(span => {
      const timestamp = span.textContent.trim();
      const fullText = span.parentElement.textContent.trim();
      const texto = fullText.startsWith(timestamp)
        ? fullText.slice(timestamp.length).trim()
        : fullText.replace(timestamp, '').trim();
      return `${timestamp}\n\n${texto}`;
    })
    .join('\n\n');

  // MONTAR OUTPUT
  const output = [
    `Módulo: ${modulo}\\`,
    `Aula: [${aulaTexto}](${pageUrl})`,
    '',
    '## Resumo da aula',
    '',
    resumo,
    '',
    '## Transcrição',
    '',
    transcricao || '[TRANSCRIÇÃO]',
    '',
    '## Resumo IA',
    '',
    '[RESUMO_IA]',
  ].join('\n');

  // Exibe no console e copia para o clipboard
  console.log(output);
  navigator.clipboard.writeText(output).then(
    () => console.log('✅ Copiado para o clipboard!'),
    () => console.warn('⚠️ Não foi possível copiar automaticamente.')
  );
})();
