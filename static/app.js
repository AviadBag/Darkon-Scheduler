const button_delete = async () => {
    const checkboxes = Array.from(document.getElementsByClassName('delete-cb'));
    for (const cb of checkboxes) {
        if (cb.checked)
            await delete_request(cb.name)
    }

    window.location.reload();
};

const delete_request = async id => {
    await fetch(`/delete/${id}`);
};