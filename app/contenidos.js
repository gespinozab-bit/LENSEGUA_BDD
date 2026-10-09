const form = document.getElementById('content-form');
const moduleInput = document.getElementById('module');
const typeInput = document.getElementById('resource-type');
const titleInput = document.getElementById('title');
const resourceInput = document.getElementById('resource-url');
const descriptionInput = document.getElementById('description');
const reviewedInput = document.getElementById('reviewed');
const message = document.getElementById('message');

const emptyState = document.getElementById('empty-state');
const contentCard = document.getElementById('content-card');
const contentModule = document.getElementById('content-module');
const contentStatus = document.getElementById('content-status');
const contentTitle = document.getElementById('content-title');
const contentResource = document.getElementById('content-resource');
const deactivateButton = document.getElementById('deactivate');
const studentList = document.getElementById('student-list');

let currentContent = null;

document.getElementById('save-draft').addEventListener('click', saveDraft);
document.getElementById('publish').addEventListener('click', publishContent);
deactivateButton.addEventListener('click', deactivateContent);

function values() {
  return {
    module: moduleInput.value,
    type: typeInput.value,
    title: titleInput.value.trim(),
    resource: resourceInput.value.trim(),
    description: descriptionInput.value.trim(),
    reviewed: reviewedInput.checked,
  };
}

function saveDraft() {
  const data = values();
  if (!data.title) {
    showMessage('El título es obligatorio para guardar el borrador', 'error');
    return;
  }

  currentContent = { ...data, status: 'Borrador' };
  renderContent();
  showMessage('Contenido guardado como borrador', 'success');
}

function publishContent() {
  const data = values();
  const validationMessage = validateForPublishing(data);
  if (validationMessage) {
    showMessage(validationMessage, 'error');
    return;
  }

  currentContent = { ...data, status: 'Publicado' };
  renderContent();
  showMessage('Contenido publicado correctamente', 'success');
}

function validateForPublishing(data) {
  if (!data.module) return 'Debe seleccionar un módulo';
  if (!data.title) return 'El título es obligatorio';
  if (!data.resource) return 'El recurso multimedia es obligatorio';
  if (!data.reviewed) return 'Debe confirmar que el material fue revisado';
  return '';
}

function deactivateContent() {
  if (!currentContent || currentContent.status !== 'Publicado') return;
  currentContent.status = 'Inactivo';
  renderContent();
  showMessage('Contenido desactivado correctamente', 'success');
}

function renderContent() {
  emptyState.hidden = true;
  contentCard.hidden = false;
  contentModule.textContent = currentContent.module || 'Sin módulo';
  contentStatus.textContent = currentContent.status;
  contentStatus.dataset.status = currentContent.status.toLowerCase();
  contentTitle.textContent = currentContent.title;
  contentResource.textContent = `${currentContent.type}: ${currentContent.resource || 'Pendiente'}`;
  deactivateButton.hidden = currentContent.status !== 'Publicado';

  studentList.innerHTML = '';
  if (currentContent.status === 'Publicado') {
    const item = document.createElement('div');
    item.id = 'student-content';
    item.className = 'student-item';
    item.innerHTML = `<strong>${escapeHtml(currentContent.title)}</strong><span>${escapeHtml(currentContent.module)}</span>`;
    studentList.appendChild(item);
  } else {
    const empty = document.createElement('span');
    empty.id = 'student-empty';
    empty.textContent = 'Sin contenidos disponibles';
    studentList.appendChild(empty);
  }
}

function showMessage(text, type) {
  message.textContent = text;
  message.className = `message ${type}`;
}

function escapeHtml(text) {
  const element = document.createElement('div');
  element.textContent = text;
  return element.innerHTML;
}

form.addEventListener('submit', (event) => event.preventDefault());
