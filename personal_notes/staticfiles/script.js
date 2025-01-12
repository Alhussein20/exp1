// Open Edit Modal
function openEditModal(id, title, description) {
    document.getElementById('editModal').style.display = 'block';
    document.getElementById('editNoteId').value = id;
    document.getElementById('editTitle').value = title;
    document.getElementById('editDescription').value = description;
}

// Submit Edit (Placeholder for actual logic)
function submitEdit() {
    const id = document.getElementById('editNoteId').value;
    const title = document.getElementById('editTitle').value;
    const description = document.getElementById('editDescription').value;

    alert(`Note Updated!\nID: ${id}\nTitle: ${title}\nDescription: ${description}`);
    closeModal('editModal');
}

// Open Delete Modal
function openDeleteModal(id, title) {
    document.getElementById('deleteModal').style.display = 'block';
    document.getElementById('deleteMessage').innerText = `Are you sure you want to delete "${title}"?`;
    window.noteToDelete = id;
}

// Confirm Delete (Placeholder for actual logic)
function confirmDelete() {
    alert(`Note ID ${window.noteToDelete} deleted.`);
    closeModal('deleteModal');
}

// Close Modals
function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

// Live Search Filter
function searchNotes() {
    const input = document.getElementById('searchInput').value.toLowerCase();
    const notes = document.getElementsByClassName('note-card');

    for (let i = 0; i < notes.length; i++) {
        const title = notes[i].getElementsByTagName('h5')[0].innerText.toLowerCase();
        notes[i].style.display = title.includes(input) ? 'block' : 'none';
    }
}
