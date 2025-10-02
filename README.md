# Rectifex Analyzer Pro-Score (Version 3.0)

This repository contains the complete codebase for the Rectifex Analyzer Pro-Score, a desktop application designed for Kubuntu. It features a FastAPI backend for data logic and a React frontend for the user interface, all containerized with Docker for development and packaged with Flatpak for desktop deployment.

### Technical Stack

*   **Backend:** Python 3.11+ with FastAPI & Poetry
*   **Database:** PostgreSQL
*   **Frontend:** React 18+ with TypeScript, Vite & Tailwind CSS
*   **Containerization:** Docker & Docker Compose
*   **Desktop Packaging:** Flatpak for Linux (Kubuntu/KDE Focus)

-----

## Entwicklungsumgebung starten (via Docker)

1.  Stelle sicher, dass Docker und Docker Compose installiert sind.
2.  Klone das Repository.
3.  Führe im Hauptverzeichnis aus: `docker-compose up --build`
4.  Das Frontend ist erreichbar unter `http://localhost:5173`.
5.  Das Backend ist erreichbar unter `http://localhost:8000/docs`.

## Flatpak-Anwendung für Kubuntu bauen und testen

1.  **Build-Tools installieren:**
    ```bash
    sudo apt update
    sudo apt install flatpak flatpak-builder
    ```

2.  **KDE Platform-Runtime hinzufügen:**
    ```bash
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
    flatpak install flathub org.kde.Platform//6.7 org.kde.Sdk//6.7
    ```

3.  **Anwendung bauen:**
    Navigiere in das Verzeichnis `packaging/flatpak` und führe aus:
    ```bash
    flatpak-builder --force-clean build-dir de.rectifex.AnalyzerProScore.yml
    ```

4.  **Anwendung installieren und starten:**
    ```bash
    flatpak-builder --user --install --force-clean build-dir de.rectifex.AnalyzerProScore.yml
    flatpak run de.rectifex.AnalyzerProScore
    ```