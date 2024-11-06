// Ensure the DOM is fully loaded before running the script
document.addEventListener('DOMContentLoaded', function () {
    let prevHoveredRow = null;
    const currentPage = document.body.getAttribute('data-page');
    console.log("Current page:", currentPage);

    // Handle row hover
    document.querySelectorAll('.hoverable-row').forEach(function (row) {

        row.addEventListener('mouseenter', function (event) {
            event.stopPropagation();

            // Remove icons from the previously hovered row, if any
            if (prevHoveredRow && prevHoveredRow !== this) {
                removeIcons(prevHoveredRow);
            }

            // Add icons on the hovered row
            if (!this.classList.contains('update-delete-icons')) {
                addIcons(this);
                prevHoveredRow = this;
            }
        });

        row.addEventListener('mouseleave', function () {
            // Remove icons when the mouse leaves the row
            if (this.classList.contains('update-delete-icons')) {
                removeIcons(this);
                prevHoveredRow = null;
            }
        });

    });

    // Function to add icons to a row
    function addIcons(row) {
        row.classList.add('update-delete-icons');

        let updateIcon = document.createElement('i');
        updateIcon.className = "fa-solid fa-pen-to-square ms-3";
        updateIcon.style.cursor = "pointer";
        updateIcon.addEventListener('click', function (event) {
            event.stopPropagation();
            openUpdateModal(row);
        })

        let deleteIcon = document.createElement('i');
        deleteIcon.className = "fa-solid fa-trash ms-3"
        deleteIcon.style.cursor = "pointer";
        deleteIcon.addEventListener('click', function (event) {
            event.stopPropagation(); // Prevent the row click event from activating
            openDeleteModal(row);
        });

        row.querySelector('td').appendChild(updateIcon);
        row.querySelector('td').appendChild(deleteIcon);
    }

    // Function to remove icons from a row
    function removeIcons(row) {
        row.classList.remove('update-delete-icons');
        let icons = row.querySelectorAll("i.fa-solid.fa-pen-to-square.ms-3, i.fa-solid.fa-trash.ms-3");
        icons.forEach(function (icon) {
            icon.remove();
        });
    }

    function openUpdateModal(row) {
        let modalId;
        switch (currentPage) {
            case 'colleges':
                modalId = 'updateCollegeModal';
                break;
            case 'courses':
                modalId = 'updateCourseModal';
                break;
            case 'students':
                modalId = 'updateStudentModal';
                break;
            default:
                console.error("No matchin modal!");
                return;
        }

        const modal = document.getElementById(modalId);
        if (!modal) {
            console.error("Modal not found!");
            return;
        }

        const dataAttributes = row.dataset;
        for (const key in dataAttributes) {
            if (dataAttributes.hasOwnProperty(key)) {
                const value = dataAttributes[key];
                console.log("Value: ", value);
                console.log("Data Attributes: ", dataAttributes);

                const modalElement = modal.querySelector(`#${key}UpdateInput`);
                console.log("Modal Element: ", modalElement);
                if (modalElement) {
                    if (key === 'photo') {
                        modalElement.src = value;
                    } else {
                        modalElement.value = value;
                    }
                }

                const hiddenInput = modal.querySelector(`#hidden${capitalizeFirstLetter(key)}`);
                if (hiddenInput) {
                    hiddenInput.value = value;
                }
            }
        }

        // Show the modal
        $(modal).modal('show');
    }

    function openDeleteModal(row) {
        console.log("Opening Delete Modal for page:", currentPage);

        let modalId;
        switch (currentPage) {
            case 'colleges':
                // $('#deleteCollegeModal').modal('show');
                modalId = 'deleteCollegeModal';
                break;
            case 'courses':
                // $('#deleteCourseModal').modal('show');
                modalId = 'deleteCourseModal';
                break;
            case 'students':
                // $('#deleteStudentModal').modal('show');
                modalId = 'deleteStudentModal';
                break;
            default:
                console.error("No matching modal!");
                return;
        }

        const modal = document.getElementById(modalId);

        if (!modal) {
            console.error("Modal not found!");
            return;
        }

        // Get all data attributes from the clicked row
        const dataAttributes = row.dataset;
        console.log("Data Attributes: ", dataAttributes)

        for (const key in dataAttributes) {
            if (dataAttributes.hasOwnProperty(key)) {
                const value = dataAttributes[key];

                // Update modal elements with matching data attributes
                const modalElement = modal.querySelector(`#${key}`);
                console.log("Modal Element: ", modalElement);
                if (modalElement) {
                    if (key === 'photo') {
                        modalElement.src = value;
                    } else {
                        modalElement.textContent = value;
                    }
                }

                // Update hidden input field, if it exists (e.g., for codes)
                const hiddenInput = modal.querySelector(`#hidden${capitalizeFirstLetter(key)}`);
                console.log("HiddenInput Element: ", hiddenInput);
                if (hiddenInput) {
                    hiddenInput.value = value;
                    console.log("HiddenInput Input: ", hiddenInput.value);
                }
            }
        }

        $(modal).modal('show');
    }

    function capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }


    // Auto-dismiss alerts
    window.setTimeout(function () {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(alert => {
            // Use Bootstrap's alert dismissal method
            alert.classList.remove('show'); // Start fade out
            alert.addEventListener('transitionend', () => alert.remove()); // Remove element after transition
        });
    }, 3000);

})