function deleteEntry(entryId){
    fetch('/delete-entry', {
        method: 'POST',
        body: JSON.stringify({ entryId: entryId }),
    }).then((_res) => {
        window.location.href='/journal';
    });
}

function deleteReminder(reminderId){
    fetch('/delete-reminder', {
        method: 'POST',
        body: JSON.stringify({ reminderId: reminderId }),
    }).then((_res) => {
        window.location.href='/reminder';
    });
}